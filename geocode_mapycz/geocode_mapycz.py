from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import json

# Geocode via Mapy.cz
def geocode_mapycz(queries, locality='', limit=1, lang='cs', cap=1000):
    """
    Geocode places via Mapy.cz using Selenium.

    Parameters:
    queries (list): Places to be queried for geocoding
    locality (string): Locations to which limit geocoding
    limit (int): Number of matches to be made per place
    lang (string): Language (abbreviation) in which to return the matches
    cap (int): Limit to number of API calls to be made

    Returns:
    dict: Payload that includes label, address, GPS coordinates, and input info
    """

    # Start Firefox (make sure its driver is in PATH)
    driver = webdriver.Firefox()

    # Load local page with simple interface for connecting to API via JS
    html = os.path.join(os.path.dirname(__file__), 'geocode_mapycz.html')
    driver.get('file://' + html)

    # Fill in details
    driver.find_element_by_id('locality').send_keys(locality)
    driver.find_element_by_id('count').send_keys(limit)
    driver.find_element_by_id('lang').send_keys(lang)

    results = {}
    for i, query in enumerate(queries):
        if i < cap:

            # Fill in query word
            cell = driver.find_element_by_id('query')
            cell.send_keys(query)
            driver.find_element_by_id('button').click()

            try:

                # Get data from alert (if it turns up)
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                res = alert.text

                output = [json.loads(i) for i in res.split('\n')]

                if output != [[]]:
                    for out in output:
                        coords = eval(out['coords'])
                        out['coords'] = (coords[1], coords[0])

                        label = out['label'].split(', ')
                        out['label'] = ', '.join(label[:-3])
                        out['address'] = ', '.join(label[-3:])

                else:
                    output = []

                alert.accept()

            except TimeoutException:

                # Fallback to empty list
                output = []

            # Get final output
            results[query] = output
            cell.clear()

            print(f'Processed by Mapy.cz: {i+1}/{len(queries)}')
        else:
            pass

    # Close Firefox
    driver.close()

    # Get final payload
    payload = {
        "queries": queries,
        "locality": locality,
        "limit": limit,
        "lang": lang,
        "results": results
    }

    return payload
