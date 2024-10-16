# Who Will Win The Election

## Overview

"Who Will Win The Election" is an analytical tool designed to assess the probabilities and outcomes of the 2024 U.S. presidential election. By compiling polling data from trusted sources, this project aims to provide insights into candidate standings, trends, and potential election outcomes.

### Current Functionality

The initial version of this project focuses on collecting and analyzing polling data from multiple sources, specifically targeting the 2024 election. Key functionalities include:

- **Data Compilation:** The tool will scrape polling data from the VoteHub Polls site and combine it with data from FiveThirtyEight to create a comprehensive dataset.
- **Data Cleaning and Organization:** The collected data will be cleaned and organized by relevant metrics such as state, party affiliation, sample size, and demographics.
- **Statistical Analysis:** The tool will analyze polling trends, average approval ratings, and confidence intervals to assess candidate viability.

Users will be able to filter the data based on specific criteria, including:

- **State vs. General Polling Trends**
- **Ideological Leanings of Pollsters**
- **Ratings of Pollsters**
- **Types of Polls Conducted**
- **Methodologies Used**
- **Demographics of Respondents**

Additionally, the tool will incorporate data on voter behavior, including:

- Likelihood of voters to vote early, vote by mail, or vote on Election Day.
- Comparisons of voter registration and ballot requests versus actual turn-ins.
- Trends in voter behavior data compared to predicted results, with insights drawn from current polling.

This comprehensive analysis will enable users to assess how these voting behaviors correlate with polling data, providing a deeper understanding of potential election outcomes.

## Future Enhancements

In the next phase, we envision expanding the project's capabilities to include automated scraping of additional trusted sources. This will allow users to input search queries into a graphical user interface (GUI), which will then gather and compile real-time data for analysis. Key enhancements include:

- **Automated Data Collection:** Users can search for specific topics or candidates, and the system will scrape relevant data from multiple trusted sources, such as news outlets and polling organizations.
- **Dynamic Data Analysis:** Users will be able to generate insights based on selected filters, utilizing averages and probabilities derived from the latest data influenced by their chosen criteria.
- **Interactive Visualizations:** Enhanced visualizations will allow users to interact with the data, exploring different scenarios and outcomes based on the filtered datasets.
- **User-Friendly Interface:** A dedicated GUI will be developed for ease of use, enabling users to navigate through the data and analyses without requiring technical expertise.

## Installation

To get started with the project, ensure you have Python installed along with the following libraries:

```bash
pip install pandas numpy beautifulsoup4 matplotlib seaborn plotly scipy statsmodels notebook
```

## License

This project is licensed under the Apache 2.0 License, allowing for use and distribution while maintaining the integrity of the original work.

## Contributing

We welcome contributions from anyone interested in enhancing this project. Please check the issues section for current needs, and feel free to submit pull requests for new features or improvements.



