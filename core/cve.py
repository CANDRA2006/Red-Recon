CVE_DB = {
    "OpenSSH": ["CVE-2016-0777", "CVE-2016-0778"],
    "Apache": ["CVE-2021-41773"],
    "MySQL": ["CVE-2019-5481"]
}

def match_cve(service):
    return CVE_DB.get(service, [])
