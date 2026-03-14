import email
import re
import sys
from email.header import decode_header


def decode_field(value):
    if not value:
        return "NOT FOUND"
    decoded_parts = decode_header(value)
    result = ""
    for part, charset in decoded_parts:
        if isinstance(part, bytes):
            result += part.decode(charset or "utf-8", errors="ignore")
        else:
            result += part
    return result.strip()


def get_body(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ("text/html", "text/plain"):
                try:
                    body += part.get_payload(decode=True).decode("utf-8", errors="ignore")
                except:
                    pass
    else:
        try:
            body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
        except:
            body = str(msg.get_payload())
    return body


def parse_email(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        msg = email.message_from_file(f)

    print("=" * 60)
    print("  EMAIL HEADER ANALYSIS")
    print("=" * 60)

    fields = ["From", "To", "Reply-To", "Return-Path",
              "Subject", "Date", "Message-ID",
              "Received-SPF", "DKIM-Signature", "X-Originating-IP"]

    for field in fields:
        value = decode_field(msg.get(field))
        print(f"  {field:<20}: {value[:80]}")

    print("\n" + "=" * 60)
    print("  RECEIVED CHAIN (Mail Path)")
    print("=" * 60)
    received = msg.get_all("Received", [])
    for i, hop in enumerate(received):
        print(f"  Hop {i+1}: {hop[:100]}")

    print("\n" + "=" * 60)
    print("  URLS EXTRACTED FROM BODY")
    print("=" * 60)
    body = get_body(msg)
    urls = re.findall(r'https?://[^\s"<>\'\)]+', body)
    if urls:
        for url in set(urls):
            print(f"  --> {url}")
    else:
        print("  No URLs found")

    print("\n" + "=" * 60)
    print("  IPs EXTRACTED")
    print("=" * 60)
    raw = open(filepath, encoding="utf-8", errors="ignore").read()
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', raw)
    if ips:
        for ip in set(ips):
            print(f"  --> {ip}")
    else:
        print("  No IPs found")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python header_parser.py <email.eml>")
    else:
        parse_email(sys.argv[1])