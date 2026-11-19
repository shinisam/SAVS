def calculate_risk(
        mismatch,
        forensic,
        metadata,
        qr_valid=True,
        signature_valid=True):

    risk = 0

    if mismatch:
        risk += 60

    if forensic:
        risk += 20

    if metadata:
        risk += 20

    if not qr_valid:
        risk += 20
        
    if signature_valid is False:

        risk += 40
    
    return risk