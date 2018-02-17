[![OpenCode](https://img.shields.io/badge/Open-Code-ff6a00.svg?style=flat-square)](https://opencode18.github.io)

# TrackMyParcelAPI

This API is used to track down details of your parcel in JSON format.
The API currently supports only E-Kart but other courier delivery agencies (like BlueDart, DTDC, etc.) would be soon added.

This API can be used to make a mobile/web application that could possibly unify all your delivery statuses in one single platform.


This will reduce the hassle to track down your couriers from variety of sites and reduce the pain to track your couriers from some really old sites.

### API ENDPOINT:

http://track-my-parcel.herokuapp.com/track/api/v1.0

You need to send the AWB Number along with the API call in a format like this:
```
http://track-my-parcel.herokuapp.com/track/api/v1.0/FMPC0278112092/
```

   Here, FMPC0278112092 is a sample AWB Number.

#### Idea Credits: [BetterClever](https://github.com/betterclever)
