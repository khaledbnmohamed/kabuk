### Web scraper


1. **Proxy Rotation**: To avoid getting blocked by the website, the script rotates between multiple proxies. This helps in masking the scraper's IP address and prevents being blacklisted.

2. **JavaScript Rendering**: The website relies on JavaScript to render hotel prices. To handle this, we used Selenium, which can interact with the website as a real user would, waiting for elements to load before attempting to extract data.

3. **Error Handling**: The script includes try-except blocks to handle any issues that might arise from using unreliable proxies. If one proxy fails, the script automatically switches to the next one.

4. **Data Storage**: Extracted data is stored in a CSV file (`hotel_prices.csv`), and a summary report is generated using Pandas, which includes descriptive statistics and is saved as `summary_report.csv`.

### Challenges Faced

- **Unreliable Free Proxies**: Free proxies are often slow or unreliable. so I skipped it and used my own IP address for the time sake
- **JavaScript Rendering**: Extracting data from a page that relies heavily on JavaScript for rendering required Selenium, which adds overhead in terms of performance but is essential for accurate data collection.

### Instructions to Run the Scraper


1. **Set Up the Virtual Environment**: 
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install Dependencies**: Run the following command to install the necessary Python packages.
   ```bash
   pip3 install requests beautifulsoup4 selenium pandas
   ```

4. **Download ChromeDriver**: Selenium requires a browser driver to interface with Chrome

5. **Run the Scraper**: Finally, execute the scraper script.
   ```bash
   python3 scraper.py
   ```

6. **Review Output**:
   - The scraper will generate a `hotel_prices.csv` file containing the scraped data.
   - A `summary_report.csv` file will also be created

### Dependencies

- Python 3.7
- `requests`
- `beautifulsoup4`
- `selenium`
- `pandas`

### Notes

- **Proxy Reliability**: Free proxies can be unreliable and that's why I skipped it and used my own IP address for this task but ideally it should be used
- **Performance**: Running the scraper with proxies and JavaScript rendering via Selenium can be slow. For a large dataset, consider optimizing the scraping process or running it on a server.
