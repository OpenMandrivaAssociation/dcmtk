#!/bin/sh
curl -L http://dicom.offis.de/dcmtk.php.en 2>/dev/null |grep -E '>dcmtk-[0-9\.]*\.tar' |sed -e 's,.*>dcmtk-,,;s,\.tar.*,,' |sort -V |tail -n1
