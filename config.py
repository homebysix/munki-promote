#!/usr/bin/python

MAKECATALOGS = "/usr/local/munki/makecatalogs"
REPO = "/Users/Shared/munki_repo"

PROMOTION_GROUPS = (
    # Promotion settings for apps on the "critical" track.
    {
        "name": "critical",
        "include_apps": ("AdobeFlashPlayer", "Silverlight"),
        "days": 2,
        "promote_from": "testing",
        "promote_to": "stable",
    },
    # Promotion settings for non-critical apps, unless excluded below.
    {
        "name": "normal",
        "include_apps": ("Atom", "Slack"),
        "days": 7,
        "promote_from": "testing",
        "promote_to": "stable",
    },
)
