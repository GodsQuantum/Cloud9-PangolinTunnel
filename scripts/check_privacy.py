#!/usr/bin/env python3
import pathlib,re,subprocess,xml.etree.ElementTree as ET
p=pathlib.Path(__file__).resolve().parent.parent
files=subprocess.check_output(['git','-C',str(p),'ls-files','-z']).decode().split(chr(0))
pat=[re.compile(x,re.I) for x in [
 'a'+'rezki', 'chou'+'gar', 'kech'+'idi', 'fe'+'lla',
 'home'+r'[.]arpa', r'192[.]168[.]', '/srv/'+'lxc/', '/home/'+'arezki',
 'gmail'+r'[.]com', '-----BEGIN PRIVATE KEY']]
bad=[]
for name in files:
 if not name or name=='scripts/check_privacy.py':continue
 f=p/name
 if not f.is_file() or f.stat().st_size>200_000:continue
 s=f.read_text(errors='replace')
 if any(x.search(s) for x in pat):bad.append(name)
if bad:raise SystemExit('PRIVATE_DATA_REVIEW_REQUIRED '+str(sorted(set(bad))))
for f in ('docs/logo.svg','docs/architecture.svg'):ET.parse(p/f)
assert (p/'patches/0001-pagination-v2.patch').is_file()
assert (p/'patches/0002-cloud9-runtime.patch').is_file()
print('PUBLIC_SOURCE_PRIVACY_SVG_AND_PATCH_CHECK_PASS')
