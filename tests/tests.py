import collector.utils.uid as UID

def test_uid():
        uid = UID.generate()
        assert len(uid) == UID.length
