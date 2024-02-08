# Django: Wedding invite web application

This is a Django web app I built for wedding invitations when I got married in 2019. 

You can use this as a template for your own wedding site or to learn more about Django.

## Installation

Clone this repo and follow the below to get this working on your PC.

1. You can set up your environment using the `requirements.txt` provided in the root directory.
2. Steps to get this up and running
   1. Run `python manage.py loaddate guest_manager/fixtures/families.json`
   1. Run `python manage.py loaddate guest_manager/fixtures/guests.json`
   2. Run `python manage.py collectstatic`
   3. Run `python manage.py makemigrations` (will ensure the necessary DBs and fixtures )
   4. Run `python manage.py migrate`
   4. Run `python manage.py runserver`

Make sure to test this using one of the below urls (specific links were sent to guests so they wouldn't have landed on the root page)

- http://127.0.0.1:8000/rsvp_viewerdx5gsvsbunb8
- http://127.0.0.1:8000/invite/fz0meudd327m
- http://127.0.0.1:8000/invite/qboeu46u1sul


## Fixtures & Models

The fixtures set up in the guest_manager app and contain information related to guests.
In here is some dummy data giving examples of what it could look like. 

The `guests.json` should contain an entry for each person attending. Each `guest` has certain attributes

- name (`str`: name to appear in invite)
- child (`boolean`: are they a child or not?)
- family_id (`int`: to link to the families fixture so make sure `family_id` in both align and all members of a single family have the same value)
- email (`str`: email address used to mail out invites)
- responded (`boolean`: have they responded?)
- attending (`boolean`: are they attending?)
- fun (`boolean`: to filter certain messaging in invite)
- message (`str`: to store any message they want to send when sending tehir RSVP)

The `families.json` should contain an entry for each person attending. Each `family` has certain attributes

- family_id (`int`: to link to the guests fixture - all members of a single family have the same value)
- url_suffix (`str`: specific randomly generated string used to identify which invite to display)
- child_allowed (`boolean`: are children allowed in this invite?)


## Invite messaging

Depending on certain parameters for given guests/families, different messaging was displayed on the invite. Here's a summary of what each field affected

- `child` - children would see options of "Can't wait to play with the cousins!" or "Sad to miss all the fun" and adults (child=0) would have options of "Ready to eat, drink, and see you get married!" or "Will toast to you from afar" displayed.
- `fun` - certain messaging at the top of the invite was changed depending on this flag. This was either tame and traditional for older generations or hinting at a wild night for younger guests. A random message is selected each time the web page loads.
- `child_allowed` - this allowed us to include specific messaging for guests with children when their children were not invited.

## Response summary page

A response summary page is included at the url `http://127.0.0.1:8000/rsvp_viewerdx5gsvsbunb8`. This captures how many responses have been recorded, by who and tallies the totals making it easy to keep track.