# Amazon Locale Tracker
Tracks new locale changes under Amazon Marketplace's CDN

## TODO:
- [X] Track CSS & Sprite changes under [/customer-preferences/country](https://www.amazon.com/customer-preferences/country)
        and [Amazon Seller Central Country Picker](https://sell.amazon.com/)
        using [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [ ] Track the [seller dropdown menu](https://www.linkedin.com/feed/update/urn:li:activity:6962836975401791490/)
    - might never happen as this requires an amazon seller central account (which none of us have), so i might have to find an alternative for this
- [X] Track domains under `/sell/navigation/logos/amazon-[top-level]`