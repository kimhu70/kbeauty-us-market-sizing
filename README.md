# Estimating US-bound Korean sheet mask exports

How much would Korean sheet mask exports to the United States be worth if sheet masks accounted for 3% of cosmetics export value? This example makes that assumption editable.

## Run the example

Unzip all three files into the same folder. Open a terminal in that folder and run with Python 3.6 or newer. The script works offline and uses only the standard library.

    python3 estimate.py --share 3

Expected output:

    2024 cosmetics exports: USD 1,899,196,000
    2025 cosmetics exports: USD 2,184,198,000
    Growth from 2024 to 2025: 15.0%
    Illustrative scenario (3% share in 2025): USD 65,525,940

Change 3 to 1 or 5 to see how much the assumption matters. Each percentage point corresponds to USD 21,841,980 in 2025.

## Data and interpretation

The CSV transcribes the US row from Table 10 of the Korean Ministry of Food and Drug Safety release dated May 22, 2026. The original unit is thousands of US dollars. [Source PDF, Table 10](https://kcia.or.kr/inc/down.php?dir=BOARD&file_name=202605_177978900248248_2.pdf)

The script multiplies the source values by 1,000 and applies the chosen percentage to the latest year. The source reports total cosmetics exports. The sheet mask share is a hypothetical input. To estimate actual US retail sales, use product-level US units sold and realized retail prices across the channels in scope.
