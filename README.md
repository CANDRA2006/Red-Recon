# Red-Recon: Asynchronous Reconnaissance Tool

## Deskripsi

Red-Recon merupakan aplikasi reconnaissance berbasis Python yang dirancang untuk keperluan **penetration testing** dan **security assessment** secara legal. Tool ini mengimplementasikan pendekatan asynchronous untuk melakukan information gathering yang efisien terhadap target domain.

---

## Fitur Utama

- **DNS Resolution**: Resolusi domain ke IP address dengan deteksi CDN berbasis IP range
- **CDN Detection**: Identifikasi Cloudflare, Akamai, Fastly, CloudFront via headers & IP
- **Security Headers Analysis**: Evaluasi 6 security headers (CSP, HSTS, X-Frame-Options, dll)
- **Dual Output Format**: JSON (structured) dan TXT (human-readable)

---

## Instalasi

```bash
git clone https://github.com/CANDRA2006/Red-Recon.git
cd Red-Recon
pip install -r requirements.txt
```

**Dependencies**: `requests`, `dnspython`, `aiohttp`

---

## Penggunaan

```bash
python cli.py <domain>

# Contoh
python cli.py example.com
```

**Output**: `output/json/report_*.json` dan `output/txt/report_*.txt`

---

## Struktur Proyek

```
Red-Recon/
│
├── cli.py                      # Entry point & orchestrasi workflow
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore config
│
├── config/
│   └── settings.py            # Global config (timeout, ports, user-agent)
│
├── core/                      # Modul inti scanning
│   ├── resolver.py            # DNS resolution + CDN detection (IP-based)
│   ├── cdn.py                 # CDN detection (header-based)
│   ├── security_headers.py    # Async security headers scanner
│   ├── scanner.py             # HTTP probing (HTTPS/HTTP fallback)
│   ├── recon.py               # Full recon orchestration
│   ├── subdomain.py           # Subdomain enum via crt.sh
│   ├── fingerprint.py         # Service identification by port
│   ├── scorer.py              # Risk scoring (HIGH/MEDIUM/LOW)
│   └── cve.py                 # CVE mapping database
│
├── utils/                     # Utility functions
│   ├── banner.py              # ASCII banner display
│   ├── writer.py              # Output handler (JSON/TXT)
│   └── logger.py              # Logging configuration
│
├── data/
│   └── wordlist.txt           # Wordlist data (future use)
│
└── output/                    # Hasil scanning
    ├── json/                  # Structured reports
    └── txt/                   # Readable reports
```

### Deskripsi File Utama

| File | Fungsi Utama |
|------|--------------|
| **cli.py** | Entry point, parse arguments, koordinasi scanning & output |
| **config/settings.py** | Konfigurasi global: `DEFAULT_TIMEOUT`, `COMMON_PORTS`, `USER_AGENT` |
| **core/resolver.py** | DNS resolution dengan `socket.gethostbyname_ex()`, deteksi Cloudflare via IP range |
| **core/cdn.py** | Deteksi CDN via HTTP headers (`Server`, `CF-Ray`, `X-Cache`, `Via`) |
| **core/security_headers.py** | Scan 6 headers: CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy |
| **core/scanner.py** | Async HTTP probing dengan timeout 5s, fallback HTTPS→HTTP |
| **utils/writer.py** | Export hasil: `save_json()` & `save_txt()` dengan auto-create directory |

---

## Workflow Eksekusi

```
cli.py
  ↓
1. show_banner()                  # Display ASCII art
2. Parse domain dari sys.argv
3. resolve_domain(domain)         # DNS → IPs → CDN check (IP)
4. scan_headers(domain)           # Async headers scan
5. save_json() & save_txt()       # Export reports
```

---

## Security Headers yang Dianalisis

| Header | Level | Fungsi |
|--------|-------|--------|
| Content-Security-Policy | Critical | Mitigasi XSS & injection |
| Strict-Transport-Security | Critical | Enforce HTTPS |
| X-Frame-Options | Important | Anti-clickjacking |
| X-Content-Type-Options | Important | Prevent MIME-sniffing |
| Referrer-Policy | Optional | Kontrol referrer info |
| Permissions-Policy | Optional | Browser permissions |

**Output**: `present` (ada) atau `missing` (tidak ada) + value & level

---

## Metodologi

**Passive Reconnaissance** - Non-intrusive information gathering:
- DNS enumeration via A records
- CDN fingerprinting (dual-method: IP range + headers)
- Security posture assessment via headers
- Asynchronous I/O untuk efisiensi

**Tidak melakukan**: Port scanning, vulnerability exploitation, active probing

---

## Use Case

1. **Security Assessment** - Evaluasi postur keamanan web application
2. **Penetration Testing** - Fase information gathering
3. **Education** - Pembelajaran reconnaissance & security headers
4. **Compliance** - Verifikasi implementasi security best practices

---

## Limitasi

- Fokus pada passive recon (no port scan/exploit)
- CDN detection terbatas 4 provider utama
- Dependency pada target availability & response time

---

## Legal Notice

⚠️ **DISCLAIMER**: Tool ini untuk **legal & educational purposes** only.

**Dilarang**:
- ❌ Scanning tanpa izin tertulis
- ❌ Unauthorized access attempt
- ❌ Malicious activities

**Diizinkan**:
- ✅ Testing sistem sendiri
- ✅ Authorized penetration testing
- ✅ Controlled learning environment

---

## Lisensi

[ MIT LICENSE](LICENSE)

## Author

**Candra**  
GitHub: [CANDRA2006/Red-Recon](https://github.com/CANDRA2006/Red-Recon)

---

**Version**: 2.0 | **Python**: ≥3.9 | **Status**: Active