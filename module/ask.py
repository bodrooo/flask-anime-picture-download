import requests as req 


class Ask():
  def __init__(self):
    self.baseUrl = ""
  
  def createUrl(self, url):
    self.baseUrl = url
  
  def get(self, url=""):
    try:
      response = req.get(self.baseUrl + url)
      response.raise_for_status()
      return response.json()
    except req.exceptions.ConnectionError as err:
      raise f"Connection error: {err}"
    except req.exceptions.HTTPError as err:
      raise f"Http error: {err}"
    except req.exceptions.RequestException as err:
      raise f"oppsss something error: {err}"
    except req.exceptions.Timeout as err:
      raise f"error timeout: {err}"
      