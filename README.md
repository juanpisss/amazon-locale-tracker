# Amazon Locale Tracker
Tracks new locale changes under Amazon Marketplace's CDN

## TODO:
- [X] Track CSS & Sprite changes under [/customer-preferences/country](https://www.amazon.com/customer-preferences/country)
        and [Amazon Seller Central Country Picker](https://sell.amazon.com/)
        using [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [ ] Track the [seller dropdown menu](https://www.linkedin.com/feed/update/urn:li:activity:6962836975401791490/)
    - might never happen as this requires an amazon seller central account (which none of us have), so i might have to find an alternative for this
- [X] Track domains under `/sell/navigation/logos/amazon-[top-level]`

## Locale Table
###### *might be out of date as i won't sustain this a lot
###### russia has been on the database for a couple of years (almost 10 years!) and due to recent political events, don't expect a release
|         G-ID          |             Country             |
| :-------------------: | :-----------------------------: |
|           1           |               USA               |
|           2           |               UK                |
|           3           |             Germany             |
|           4           |               ???               |
|           5           |               ???               |
|           6           |               ???               |
|           8           |             France              |
|           9           |              Japan              |
|          15           |             Canada              |
|       ***16***        |          ***Target***           |
|        **17**         |             **???**             |
|        **18**         |             **???**             |
|        **19**         |             **???**             |
|          28           |              China              |
|          29           |              Italy              |
|          30           |              Spain              |
|          31           |              India              |
|          32           |             Brazil              |
|          33           |             Mexico              |
| <font size="3">**34** |    <font size="3">**Russia**    |
|          35           |            Australia            |
|          37           |           Netherlands           |
| <font size="5">**38** |     <font size="5">**???**      |
|          39           |               UAE               |
|          40           |          Saudi Arabia           |
|          41           |             Turkey              |
|          42           |              Egypt              |
| <font size="5">**43** |     <font size="5">**???**      |
|          46           |             Sweden              |
|          48           |             Poland              |
| <font size="5">**49** |   <font size="5">**Colombia**   |
| <font size="5">**50** |    <font size="5">**Chile**     |
| <font size="5">**51** |   <font size="5">**Belgium**    |
| <font size="5">**52** |   <font size="5">**Nigeria**    |
| <font size="5">**53** | <font size="5">**South Africa** |
|          65           |            Singapore            |

