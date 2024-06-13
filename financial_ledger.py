financial_ledger= {
    # Assets
    "Cash and Cash Equivalents": {
        "English": ["cash and cash equivalents", "cash", "cash on hand", "liquid assets", "treasury bills", "certificates of deposit", "undeposited receipts", "money market funds"],
        "Dutch": ["contanten en kasequivalenten", "contanten", "liquide middelen", "kasgeld", "schatkistbiljetten", "certificaten van deposito", "niet-gedeponeerde ontvangsten", "geldmarktfondsen"],
        "balance": "debit",
        "id": "CashAndCashEquivalents",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "240"
    },
    "Marketable Securities": {
        "English": ["marketable securities", "commercial paper", "treasury notes", "money market instruments"],
        "Dutch": ["verhandelbare effecten", "handelspapier", "schatkistpromessen", "geldmarktinstrumenten"],
        "balance": "debit",
        "id": "MarketableSecurities",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "130"
    },
    "Accounts Receivable": {
        "English": ["accounts receivable", "trade receivables", "debtor's balance", "amounts owed by customers", "money owed by customers"],
        "Dutch": ["debiteuren", "handelsvorderingen", "vorderingen", "door klanten verschuldigd geld"],
        "balance": "debit",
        "id": "AccountsReceivable",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "220"
    },
    "Inventories": {
        "English": ["inventories", "stock", "goods", "merchandise", "finished goods", "work in progress", "raw materials"],
        "Dutch": ["voorraden", "voorraad", "inventaris", "goederenvoorraad", "gereed product", "onderhanden werk", "grondstoffen"],
        "balance": "debit",
        "id": "Inventories",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "210"
    },
    "Prepaid Expenses": {
        "English": ["prepaid expenses", "costs paid in advance", "prepayments"],
        "Dutch": ["vooruitbetaalde kosten", "overlopende activa", "vooruitbetalingen"],
        "balance": "debit",
        "id": "PrepaidExpenses",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "299"
    },
    "Property, Plant, and Equipment": {
        "English": ["property, plant, and equipment", "PPE", "fixed assets", "buildings", "machinery", "long-term assets", "physical assets", "tangible fixed assets", "property, plant and equipment machinery"],
        "Dutch": ["materiële vaste activa", "vaste activa", "gebouwen", "machines", "langetermijnactiva", "tastbare vaste activa"],
        "balance": "debit",
        "id": "PropertyPlantAndEquipment",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "120"
    },
    "Intangible Assets": {
        "English": ["intangible assets", "goodwill", "patents", "trademarks", "copyrights"],
        "Dutch": ["immateriële activa", "goodwill", "patenten", "handelsmerken", "auteursrechten"],
        "balance": "debit",
        "id": "IntangibleAssets",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"110"
    },

    # Liabilities
    "Current Liabilities": {
        "English": ["short-term liabilities", "current liabilities", "trade creditors", "payments received for not yet delivered services", "loans due within one year", "portion of long-term debt due within next year", "expenses incurred but not yet paid"],
        "Dutch": ["kortlopende verplichtingen", "actuele verplichtingen", "handelscrediteuren", "ontvangen betalingen voor nog niet geleverde diensten", "leningen die binnen een jaar verschuldigd zijn", "deel van langlopende schuld dat binnen het volgende jaar verschuldigd is", "gemaakte kosten maar nog niet betaald"],
        "balance": "credit",
        "id": "CurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode": "450"
    },
    
    "Long-term Liabilities": {
        "English": ["long-term liabilities", "debentures", "mortgage bonds", "long-term loans", "loans not due within the next year"],
        "Dutch": ["langlopende verplichtingen", "niet-actuele verplichtingen", "obligaties", "hypothecaire obligaties", "overige leningen", "leningen die niet binnen het volgende jaar verschuldigd zijn"],
        "balance": "credit",
        "id": "LongTermLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"440"
    },

    # Equity
    "Shareholder's Equity": {
        "English": ["stockholder's equity", "owners' equity", "shareholders' funds", "money received from investors", "cumulative earnings not distributed"],
        "Dutch": ["eigen vermogen", "aandeelhouderskapitaal", "van investeerders ontvangen geld", "cumulatieve winsten niet uitgekeerd"],
        "balance": "credit",
        "id": "ShareholdersEquity",
        "category": "equity",
        "statement_type": "balance_sheet",
        "postencode":"300"
    },

    # Revenue
    "Revenue": {
        "English": ["sales", "income", "turnover", "sales revenue", "net sales", "income from goods sold", "income from services provided"],
        "Dutch": ["omzet", "inkomsten", "opbrengsten", "netto-omzet", "verkoopopbrengsten", "inkomsten uit verkochte goederen", "inkomsten uit verleende diensten"],
        "balance": "credit",
        "id": "Revenue",
        "category": "revenue",
        "statement_type": "income_statement",
        "postencode":"810"
    },

    # Expenses
    "Expenses": {
        "English": ["cost of sales", "cost of revenue", "direct costs attributable to goods sold", "expenses related to business operations", "rent", "utilities", "salaries", "expense for reduction in value of assets"],
        "Dutch": ["kostprijs van de verkopen", "kosten van de omzet", "rechtstreekse kosten toe te rekenen aan verkochte goederen", "bedrijfskosten", "huur", "nutsvoorzieningen", "salarissen", "kosten voor waardevermindering van activa"],
        "balance": "debit",
        "id": "Expenses",
        "category": "expenses",
        "statement_type": "income_statement",
        "postencode":"710"
    },

    # Net Income
    "Net Income": {
        "English": ["net profit", "net earnings", "bottom line", "final profit after all expenses", "operating profit", "operating loss", "pre-tax profit", "pre-tax loss"],
        "Dutch": ["nettowinst", "netto inkomen", "uiteindelijke winst na alle kosten", "bedrijfsresultaat", "exploitatieresultaat", "resultaat voor belasting", "resultaat na belastingen"],
        "balance": "debit",
        "id": "NetIncome",
        "category": "revenue",
        "statement_type": "income_statement",
        "postencode":"900"
    },
    
      "Accounts Payable": {
        "English": ["accounts payable", "obligations to suppliers", "creditors"],
        "Dutch": ["crediteuren", "verplichtingen aan leveranciers", "leveranciersschuld"],
        "balance": "credit",
        "id": "AccountsPayable",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode": "455"
    },
    "Unearned Revenue": {
        "English": ["unearned revenue", "payments received for goods or services not yet delivered", "deferred revenue"],
        "Dutch": ["ontvangen opbrengsten", "vooruitontvangen betalingen voor nog niet geleverde goederen of diensten", "uitgestelde opbrengsten"],
        "balance": "credit",
        "id": "UnearnedRevenue",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode": "450"
    },
    "Short-term Debt": {
        "English": ["short-term debt", "loans and borrowings due within one year", "current debt"],
        "Dutch": ["korte-termijnschulden", "leningen en kredieten die binnen een jaar verschuldigd zijn", "lopende schulden"],
        "balance": "credit",
        "id": "ShortTermDebt",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode": "450"
    },
    "Current Portion of Long-term Debt": {
        "English": ["current portion of long-term debt", "the portion of long-term debt due within the next year"],
        "Dutch": ["kortlopend deel van de langlopende schuld", "deel van de langlopende schuld dat binnen het volgende jaar verschuldigd is"],
        "balance": "credit",
        "id": "CurrentPortionOfLongTermDebt",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode": "456"
    },
    "Other Accrued Expenses and Liabilities": {
        "English": ["other accrued expenses and liabilities", "expenses incurred but not yet paid"],
        "Dutch": ["overige opgelopen kosten en verplichtingen", "gemaakte kosten maar nog niet betaald"],
        "balance": "credit",
        "id": "OtherAccruedExpensesAndLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode": "456"
    },
    "Long-term Debt": {
        "English": ["long-term debt", "loans and borrowings not due within the next year"],
        "Dutch": ["langlopende schuld", "leningen en kredieten die niet binnen het volgende jaar verschuldigd zijn"],
        "balance": "credit",
        "id": "LongTermDebt",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"440"
    },
    "Current Receivables": {
        "English": ["current receivables from other legal entities and companies with a participating interest", "receivables from affiliates", "receivables from associated companies", 'current assets receivables trade receivables', 'receivables trade receivables', 'taxes and social security charges'],
        "Dutch": ["vorderingen op andere rechtspersonen en vennootschappen met een deelnemingsbelang", "vorderingen op gelieerde ondernemingen", "vorderingen op deelnemende ondernemingen"],
        "balance": "debit",
        "id": "CurrentReceivablesFromOtherEntities",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"299"
    },
    
    "Total of Receivables": {
        "English": ["total of receivables", "aggregate receivables", "sum of receivables"],
        "Dutch": ["totaal vorderingen", "geaggregeerde vorderingen", "som van vorderingen"],
        "balance": "debit",
        "id": "TotalOfReceivables",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "220"
    },
    
    "Depreciation of Property, Plant, and Equipment": {
        "English": ["depreciation of property, plant, and equipment", "amortisation of property, plant, and equipment", "depreciation", "amortization of tangible assets", "depreciation of property, plant and equipment"],
        "Dutch": ["afschrijvingen op materiële vaste activa", "afschrijvingen", "amortisatie van materiële vaste activa"],
        "balance": "debit",
        "id": "DepreciationOfPPE",
        "category": "expenses",
        "statement_type": "income_statement",
        "postencode":"725"
    },
    "Inventories under Construction": {
        "English": ["inventories under construction", "construction in progress", "work in progress"],
        "Dutch": ["onderhanden werk", "bouw in uitvoering", "werk in uitvoering"],
        "balance": "debit",
        "id": "InventoriesUnderConstruction",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"210"
    },
    "Finished and Trade Goods": {
        "English": ["finished and trade goods", "finished goods", "merchandise", "trading stock"],
        "Dutch": ["gereed product en handelsgoederen", "afgewerkte producten", "handelswaren", "handelsvoorraad"],
        "balance": "debit",
        "id": "FinishedAndTradeGoods",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"210"
    },
    "Total of Inventories": {
        "English": ["total of inventories", "total inventories", "aggregate inventories"],
        "Dutch": ["totaal voorraden", "totale voorraden", "geaggregeerde voorraden"],
        "balance": "debit",
        "id": "TotalOfInventories",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"210"
    },
    "Receivables Trade Receivables": {
        "English": ["receivables trade receivables", "trade receivables", "accounts receivable", "debtors"],
        "Dutch": ["handelsvorderingen", "vorderingen uit handel", "debiteuren", "rekeningen te ontvangen"],
        "balance": "debit",
        "id": "ReceivablesTradeReceivables",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"220"
    },
    "Taxes and Social Security Charges": {
        "English": ["taxes and social security charges", "tax receivables", "government receivables"],
        "Dutch": ["belastingen en sociale zekerheidsbijdragen", "belastingvorderingen", "overheidsvorderingen"],
        "balance": "debit",
        "id": "TaxesAndSocialSecurityCharges",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"255"
    },
    "not applicable": {
        "English": ["not applicable", "the text does not mention any category name", " i cannot extract the requested data"],
        "Dutch" : ["not applicable", " the text does not mention any category name", " i cannot extract the requested data"],
        "balance": "none",
        "id": "none",
        "category": "none",
        "statement_type": "none",
        "postencode":"0"
    },
    "Inventories Under Construction": {
        "English": ["inventories under construction"],
        "Dutch": ["onderhanden werk"],
        "balance": "debit",
        "id": "InventoriesUnderConstruction",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"210"
    },
    "Prepayments and Accrued Income": {
        "English": ["prepayments", "accrued income", "prepaid income"],
        "Dutch": ["vooruitbetalingen", "overlopende activa", "vooruitbetaalde inkomsten"],
        "balance": "debit",
        "id": "PrepaymentsAndAccruedIncome",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode": "299"
    },
    "Total of Current Assets": {
        "English": ["total of current assets"],
        "Dutch": ["totaal vlottende activa"],
        "balance": "debit",
        "id": "TotalOfCurrentAssets",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"200"
    },
    "Total of Assets": {
        "English": ["total of assets"],
        "Dutch": ["totaal activa"],
        "balance": "debit",
        "id": "TotalOfAssets",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"1"
    },
    "Group Equity": {
        "English": ["group equity", "consolidated equity"],
        "Dutch": ["groepsvermogen", "geconsolideerd eigen vermogen"],
        "balance": "credit",
        "id": "GroupEquity",
        "category": "equity",
        "statement_type": "balance_sheet",
        "postencode": "410"
    },
    "Non-Current Liabilities": {
        "English": ["non-current liabilities", "debentures", "mortgage bonds", "other loans", "debentures", "mortgage bonds", "other loans"],
        "Dutch": ["niet-vlottende passiva", "obligaties", "hypotheekobligaties", "overige leningen"],
        "balance": "credit",
        "id": "NonCurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"440"
    },
    "Total of Non-Current Liabilities": {
        "English": ["total of non-current liabilities"],
        "Dutch": ["totaal niet-vlottende passiva"],
        "balance": "credit",
        "id": "TotalOfNonCurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"400"
    },
    "Total of Current Liabilities": {
        "English": ["total of current liabilities"],
        "Dutch": ["totaal kortlopende passiva"],
        "balance": "credit",
        "id": "TotalOfCurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"400"
    },
    "Total of Equity and Liabilities": {
        "English": ["total of equity and liabilities"],
        "Dutch": ["totaal eigen vermogen en passiva"],
        "balance": "credit",
        "id": "TotalOfEquityAndLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"1"
    },
    "Severance Payments": {
        "English": ["severance payments"],
        "Dutch": ["ontslagvergoedingen"],
        "balance": "debit",
        "id": "SeverancePayments",
        "category": "expenses",
        "statement_type": "income_statement",
        "postencode":"715"
    },
    "Total of Expenses of Employee Benefits": {
        "English": ["total of expenses of employee benefits"],
        "Dutch": ["totaal personeelskosten"],
        "balance": "debit",
        "id": "TotalOfExpensesOfEmployeeBenefits",
        "category": "expenses",
        "statement_type": "income_statement",
        "postencode":"705"
    },
       "Income Tax Expense": {
        "English": ["income tax expense"],
        "Dutch": ["inkomstenbelasting"],
        "balance": "debit",
        "id": "IncomeTaxExpense",
        "category": "expenses",
        "statement_type": "income_statement",
        "postencode":"770"
    },
    "Share in Results of Participating Interests": {
        "English": ["share in results of participating interests"],
        "Dutch": ["deel in resultaten van deelnemende belangen"],
        "balance": "credit",
        "id": "ShareInResultsOfParticipatingInterests",
        "category": "revenue",
        "statement_type": "income_statement",
        "postencode":"863"
    },
    "Operating Result": {
        "English": ["operating result"],
        "Dutch": ["bedrijfsresultaat"],
        "balance": "either",
        "id": "OperatingResult",
        "category": "result",
        "statement_type": "income_statement",
        "postencode":"827"
    },
    "Other Interest Income and Related Income": {
        "English": ["other interest income and related income", "revenues from other receivables", "other revenues from other receivables"],
        "Dutch": ["overige rentebaten en soortgelijke opbrengsten", "opbrengsten uit andere vorderingen", "andere opbrengsten uit andere vorderingen"],
        "balance": "credit",
        "id": "OtherInterestIncomeAndRelatedIncome",
        "category": "revenue",
        "statement_type": "income_statement",
        "postencode":"831"
    },
    "Interest Expenses and Related Expenses": {
        "English": ["interest expenses and related expenses", "costs on liabilities", "other interest expenses"],
        "Dutch": ["rente- en soortgelijke kosten", "kosten voor verplichtingen", "overige rentekosten"],
        "balance": "debit",
        "id": "InterestExpensesAndRelatedExpenses",
        "category": "expenses",
        "statement_type": "income_statement",
        "postencode":"730"
    },
    "Non Current Assets": {
        "English": ["non-current assets", "other tangible assets", "long-term assets", "fixed assets"],
        "Dutch": ["niet-vlottende activa", "overige materiële activa", "langetermijnactiva", "vaste activa"],
        "balance": "debit",
        "id": "NonCurrentAssets",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"120"
    },
    "Total of Non Current Assets": {
        "English": ["total of non-current assets", "aggregate non-current assets"],
        "Dutch": ["totaal niet-vlottende activa", "totaal langetermijnactiva"],
        "balance": "debit",
        "id": "TotalOfNonCurrentAssets",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"100"
    },
    "Financial Assets": {
        "English": ["financial assets", "investment securities", "held-to-maturity investments"],
        "Dutch": ["financiële activa", "beleggingswaarden", "beleggingen tot einde looptijd"],
        "balance": "debit",
        "id": "FinancialAssets",
        "category": "assets",
        "statement_type": "balance_sheet",
        "postencode":"130"
    },
    "Repayment Obligations of Non Current Borrowings": {
        "English": ["repayment obligations of non-current borrowings", "long-term debt repayments"],
        "Dutch": ["aflossingsverplichtingen van niet-vlottende leningen", "afbetalingen op langlopende schulden"],
        "balance": "credit",
        "id": "RepaymentObligationsOfNonCurrentBorrowings",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"440"
    },
    "Accruals and Deferred Income": {
        "English": ["accruals and deferred income", "deferred revenues", "accrued liabilities"],
        "Dutch": ["overlopende passiva en uitgestelde inkomsten", "uitgestelde opbrengsten", "opgelopen verplichtingen"],
        "balance": "credit",
        "id": "AccrualsAndDeferredIncome",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"499"
    },
    "Operating Income": {
        "English": ["other operating income", "total operating income", "business income", "operating revenues", "total operating income net revenue"],
        "Dutch": ["overige bedrijfsopbrengsten", "totaal bedrijfsopbrengsten", "bedrijfsinkomsten", "exploitatieopbrengsten"],
        "balance": "credit",
        "id": "OperatingIncome",
        "category": "revenue",
        "statement_type": "income_statement",
        "postencode":"810"
    },
    "Payables": {
        "English": ["payables to banks", "payables relating to taxes and social security contributions", "payables to taxes and social security contributions", "payables to social security contributions", "payables relating to taxes and social security contributions value added tax"],
        "Dutch": ["schulden aan banken", "verplichtingen met betrekking tot belastingen en sociale zekerheidsbijdragen", "btw-verplichtingen"],
        "balance": "credit",
        "id": "Payables",
        "category": "liabilities",
        "statement_type": "balance_sheet",
        "postencode":"450"
    },
    "Operating Expenses": {
        "English": ["operating expenses", "expenses of employee benefits wages", "car and transport costs", "office related expenses", "general expenses", "total of other operating expenses", "administrative expenses", "selling expenses"],
        "Dutch": ["bedrijfskosten", "personeelskosten lonen", "auto- en transportkosten", "kantoorkosten", "algemene kosten", "totaal overige bedrijfskosten", "administratieve kosten", "verkoopkosten"],
        "balance": "debit",
        "id": "OperatingExpenses",
        "category": "expenses",
        "statement_type": "income_statement",
        "postencode":"735"   
    },
    "Requested Capital": {
    "English": ["requested capital", "called-up share capital", "subscribed capital", "capital called up"],
    "Dutch": ["gestort en opgevraagd kapitaal", "gestort kapitaal", "opgevraagd kapitaal"],
    "balance": "credit",
    "id": "RequestedCapital",
    "category": "equity",
    "statement_type": "balance_sheet",
    "postencode": "310"
  },
  "Revaluation Reserve": {
    "English": ["revaluation reserve", "revaluation surplus", "valuation reserve"],
    "Dutch": ["herwaarderingsreserve"],
    "balance": "credit",
    "id": "RevaluationReserve",
    "category": "equity",
    "statement_type": "balance_sheet",
    "postencode": "330"
  },
  "Undivided Profit": {
    "English": ["undivided profit", "retained earnings", "accumulated profit"],
    "Dutch": ["onverdeelde winst"],
    "balance": "credit",
    "id": "UndividedProfit",
    "category": "equity",
    "statement_type": "balance_sheet",
    "postencode": "360"
  },
  "Other Fixed Assets": {
    "English": ["other fixed assets", "non-current assets", "fixed asset investments"],
    "Dutch": ["overige vaste activa"],
    "balance": "debit",
    "id": "OtherFixedAssets",
    "category": "assets",
    "statement_type": "balance_sheet",
    "postencode": "199"
  },
  "Effects": {
    "English": ["effects", "securities", "financial instruments"],
    "Dutch": ["effecten"],
    "balance": "debit",
    "id": "Effects",
    "category": "assets",
    "statement_type": "balance_sheet",
    "postencode": "230"
  },
  "Premium": {
    "English": ["premium", "share premium", "additional paid-in capital"],
    "Dutch": ["agio"],
    "balance": "credit",
    "id": "Premium",
    "category": "equity",
    "statement_type": "balance_sheet",
    "postencode": "320"
  },
  "Lawt And Stat Reserves": {
    "English": ["lawt. and stat. reserves", "legal reserves", "statutory reserves"],
    "Dutch": ["wettelijke en statutaire reserves"],
    "balance": "credit",
    "id": "LawtAndStatReserves",
    "category": "equity",
    "statement_type": "balance_sheet",
    "postencode": "340"
  },
  "Other Reserves": {
    "English": ["other reserves", "general reserves", "various reserves"],
    "Dutch": ["overige reserves"],
    "balance": "credit",
    "id": "OtherReserves",
    "category": "equity",
    "statement_type": "balance_sheet",
    "postencode": "350"
  },
  "Equalization Account": {
    "English": ["equalization account", "equalization provision"],
    "Dutch": ["egalisatierekening"],
    "balance": "debit",
    "id": "EqualizationAccount",
    "category": "liabilities",
    "statement_type": "balance_sheet",
    "postencode": "420"
  },
  "Services": {
    "English": ["services", "provisions for services"],
    "Dutch": ["voorzieningen voor diensten"],
    "balance": "debit",
    "id": "Services",
    "category": "liabilities",
    "statement_type": "balance_sheet",
    "postencode": "430"
  },
  "Third Party Share": {
    "English": ["third party share", "minority interest"],
    "Dutch": ["aandeel derden"],
    "balance": "credit",
    "id": "ThirdPartyShare",
    "category": "equity",
    "statement_type": "balance_sheet",
    "postencode": "460"
  },
  "Sales And Management Costs": {
    "English": ["sales and management costs", "selling and administrative expenses"],
    "Dutch": ["verkoop- en beheerskosten"],
    "balance": "debit",
    "id": "SalesAndManagementCosts",
    "category": "expenses",
    "statement_type": "income_statement",
    "postencode": "720"
  },
  "Charge From Company Exercise": {
    "English": ["charge from company exercise"],
    "Dutch": ["belasting uit bedrijfsoefening"],
    "balance": "debit",
    "id": "ChargeFromCompanyExercise",
    "category": "expenses",
    "statement_type": "income_statement",
    "postencode": "740"
  },
  "Extraordinary Expenses": {
    "English": ["extraordinary expenses", "exceptional charges"],
    "Dutch": ["buitengewone lasten"],
    "balance": "debit",
    "id": "ExtraordinaryExpenses",
    "category": "expenses",
    "statement_type": "income_statement",
    "postencode": "750"
  },
  "Charge on Outdoor Reslts": {
    "English": ["charge on outdoor results", "extraordinary costs"],
    "Dutch": ["belasting op buitengewone resultaten"],
    "balance": "debit",
    "id": "ChargeOutdoorRsltt",
    "category": "expenses",
    "statement_type": "income_statement",
    "postencode": "760"
  },
  "Other Operating Income": {
    "English": ["other operating income", "miscellaneous operating income"],
    "Dutch": ["overige bedrijfsopbrengsten"],
    "balance": "credit",
    "id": "OvOperatingIncome",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "820"
  },
  "Financial Benefits": {
    "English": ["financial benefits", "financial income", "investment income"],
    "Dutch": ["financiële baten"],
    "balance": "credit",
    "id": "FinancialBenefits",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "830"
  },
  "Extraordinary Income": {
    "English": ["extraordinary income", "non-recurring income", "exceptional income"],
    "Dutch": ["buitengewone baten"],
    "balance": "credit",
    "id": "ExtraordinaryIncome",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "840"
  },
  "Result From Share After tax": {
    "English": ["results from share after tax", "earnings from investments post-tax"],
    "Dutch": ["resultaat uit deelnemingen na belasting"],
    "balance": "credit",
    "id": "ResultFromShareAfterBell",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "860"
  },
  "balance of gains and losses after tax": {
    "English": ["balance of gains and losses after tax", "net gains after tax"],
    "Dutch": ["saldo van baten en lasten na belasting"],
    "balance": "credit or debit",
    "id": "SldOvBtnAndLstnAfterBell",
    "category": "revenue or expenses",
    "statement_type": "income_statement",
    "postencode": "870"
  },
  "Third Party Share In Results": {
    "English": ["third party share in results", "minority interest in profits"],
    "Dutch": ["aandeel derden in het resultaat"],
    "balance": "credit",
    "id": "ThirdPartyShareInResults",
    "category": "equity",
    "statement_type": "income_statement",
    "postencode": "780"
  },
  "Balance Loss": {
    "English": ["balance loss", "net loss"],
    "Dutch": ["saldo verlies"],
    "balance": "debit",
    "id": "BalanceLoss",
    "category": "expenses",
    "statement_type": "income_statement",
    "postencode": "370"
  },
  "Sum Of Operating Income": {
    "English": ["sum of operating income", "total operating revenue"],
    "Dutch": ["som bedrijfsopbrengsten"],
    "balance": "credit",
    "id": "SumOfOperatingIncome",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "805"
  },
  "Gross Sales Result": {
    "English": ["gross sales result", "gross revenue from sales"],
    "Dutch": ["bruto-omzetresultaat"],
    "balance": "credit",
    "id": "GrossSalesResult",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "825"
  },
    "Change In Inventories": {
    "English": ["change in inventories", "inventory adjustments", "stock variations"],
    "Dutch": ["wijziging in voorraden"],
    "balance": "credit or debit",
    "id": "ChangeInInventories",
    "category": "current assets or expenses",
    "statement_type": "income_statement",
    "postencode": "811"
  },
  "Activated Production": {
    "English": ["activated production", "capitalized production", "production costs activated"],
    "Dutch": ["geactiveerde productie"],
    "balance": "debit",
    "id": "ActivatedProduction",
    "category": "assets",
    "statement_type": "balance_sheet",
    "postencode": "812"
  },
  "Results From Business Operation Pre Tax": {
    "English": ["results from business operations before tax", "pre-tax operating profit"],
    "Dutch": ["resultaat uit bedrijfsoefening voor belasting"],
    "balance": "credit",
    "id": "ResultsFromBusinessOperationPreTax",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "835"
  },
  "Results From Business Operation Net Of Calls": {
    "English": ["results from business operations net of calls", "net operating profit after adjustments"],
    "Dutch": ["resultaat uit bedrijfsoefening na belasting"],
    "balance": "credit",
    "id": "ResultsFromBusinessOperationNetOfCalls",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "837"
  },
  "Balance Outside Income Expenses": {
    "English": ["balance of outside income/expenses", "net non-operating income/expenses"],
    "Dutch": ["saldo van buitengewone baten en lasten"],
    "balance": "credit or debit",
    "id": "BalanceOutsideIncomeExpenses",
    "category": "revenue or expenses",
    "statement_type": "income_statement",
    "postencode": "841"
  },
  "Extraordinary Results After Tax": {
    "English": ["extraordinary results after tax", "post-tax extraordinary income"],
    "Dutch": ["buitengewone resultaten na belasting"],
    "balance": "credit",
    "id": "ExtraordinaryResultsAfterTax",
    "category": "revenue",
    "statement_type": "income_statement",
    "postencode": "850"
  }
 }


def get_terms(term, language):
    """
    Retrieve the synonyms and translations for a given term and language.
    
    :param term: The financial term to look up (e.g., "Revenue")
    :param language: The language for synonyms and translations ("English" or "Dutch")
    :return: A list of terms in the specified language
    """
    return financial_ledger.get(term, {}).get(language, [])


