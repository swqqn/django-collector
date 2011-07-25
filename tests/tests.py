from collector.models import Blob
import collector.utils.uid as UID

import django.db

import nose.tools


def __uid(length, characters):
        __length = UID.length
        __characters = UID.characters

        UID.length = length
        UID.characters = characters

        uid = UID.generate()

        UID.length = __length
        UID.characters = __characters

        return uid


def test_uid():
        __length = UID.length
        __characters = UID.characters

        uid = __uid(UID.length, UID.characters)

        assert len(uid) == UID.length

        for x in uid:
                assert x in UID.characters

        uid = __uid(128, UID.characters)

        assert len(uid) == 128

        for x in uid:
                assert x in UID.characters

        uid = __uid(UID.length, 'xX')

        assert len(uid) == UID.length

        for x in uid:
                assert x in 'xX'

        uid = __uid(128, 'xX')

        assert len(uid) == 128

        for x in uid:
                assert x in 'xX'

        assert __length == UID.length
        assert __characters == UID.characters


@nose.tools.raises(django.db.IntegrityError)
def __unique():
        blob1 = Blob()
        blob2 = Blob()

        blob1.uid = blob2.uid = 'UID'

        blob1.save()
        blob2.save()


def test_models():
        email = 'example@example.com'

        blob = Blob()

        assert len(blob.uid) == UID.length
        assert blob.email == ''

        blob.email = email
        blob.save()

        assert blob.email == email

        __unique()

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
