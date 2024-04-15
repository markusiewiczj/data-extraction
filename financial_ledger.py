financial_ledger= {
    # Assets
    "Cash and Cash Equivalents": {
        "English": ["cash and cash equivalents", "cash", "cash on hand", "liquid assets", "treasury bills", "certificates of deposit", "undeposited receipts", "money market funds"],
        "Dutch": ["contanten en kasequivalenten", "contanten", "liquide middelen", "kasgeld", "schatkistbiljetten", "certificaten van deposito", "niet-gedeponeerde ontvangsten", "geldmarktfondsen"],
        "balance": "debit",
        "id": "CashAndCashEquivalents",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Marketable Securities": {
        "English": ["marketable securities", "commercial paper", "treasury notes", "money market instruments"],
        "Dutch": ["verhandelbare effecten", "handelspapier", "schatkistpromessen", "geldmarktinstrumenten"],
        "balance": "debit",
        "id": "MarketableSecurities",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Accounts Receivable": {
        "English": ["accounts receivable", "trade receivables", "debtor's balance", "amounts owed by customers", "money owed by customers"],
        "Dutch": ["debiteuren", "handelsvorderingen", "vorderingen", "door klanten verschuldigd geld"],
        "balance": "debit",
        "id": "AccountsReceivable",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Inventories": {
        "English": ["inventories", "stock", "goods", "merchandise", "finished goods", "work in progress", "raw materials"],
        "Dutch": ["voorraden", "voorraad", "inventaris", "goederenvoorraad", "gereed product", "onderhanden werk", "grondstoffen"],
        "balance": "debit",
        "id": "Inventories",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Prepaid Expenses": {
        "English": ["prepaid expenses", "costs paid in advance"],
        "Dutch": ["vooruitbetaalde kosten", "overlopende activa"],
        "balance": "debit",
        "id": "PrepaidExpenses",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Property, Plant, and Equipment": {
        "English": ["property, plant, and equipment", "PPE", "fixed assets", "buildings", "machinery", "long-term assets", "physical assets", "tangible fixed assets", "property, plant and equipment machinery"],
        "Dutch": ["materiële vaste activa", "vaste activa", "gebouwen", "machines", "langetermijnactiva", "tastbare vaste activa"],
        "balance": "debit",
        "id": "PropertyPlantAndEquipment",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Intangible Assets": {
        "English": ["intangible assets", "goodwill", "patents", "trademarks", "copyrights"],
        "Dutch": ["immateriële activa", "goodwill", "patenten", "handelsmerken", "auteursrechten"],
        "balance": "debit",
        "id": "IntangibleAssets",
        "category": "assets",
        "statement_type": "balance_sheet"
    },

    # Liabilities
    "Current Liabilities": {
        "English": ["short-term liabilities", "current liabilities", "trade creditors", "payments received for not yet delivered services", "loans due within one year", "portion of long-term debt due within next year", "expenses incurred but not yet paid"],
        "Dutch": ["kortlopende verplichtingen", "actuele verplichtingen", "handelscrediteuren", "ontvangen betalingen voor nog niet geleverde diensten", "leningen die binnen een jaar verschuldigd zijn", "deel van langlopende schuld dat binnen het volgende jaar verschuldigd is", "gemaakte kosten maar nog niet betaald"],
        "balance": "credit",
        "id": "CurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    
    "Long-term Liabilities": {
        "English": ["long-term liabilities", "debentures", "mortgage bonds", "long-term loans", "loans not due within the next year"],
        "Dutch": ["langlopende verplichtingen", "niet-actuele verplichtingen", "obligaties", "hypothecaire obligaties", "overige leningen", "leningen die niet binnen het volgende jaar verschuldigd zijn"],
        "balance": "credit",
        "id": "LongTermLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },

    # Equity
    "Shareholder's Equity": {
        "English": ["stockholder's equity", "owners' equity", "shareholders' funds", "money received from investors", "cumulative earnings not distributed"],
        "Dutch": ["eigen vermogen", "aandeelhouderskapitaal", "van investeerders ontvangen geld", "cumulatieve winsten niet uitgekeerd"],
        "balance": "credit",
        "id": "ShareholdersEquity",
        "category": "equity",
        "statement_type": "balance_sheet"
    },

    # Revenue
    "Revenue": {
        "English": ["sales", "income", "turnover", "sales revenue", "net sales", "income from goods sold", "income from services provided"],
        "Dutch": ["omzet", "inkomsten", "opbrengsten", "netto-omzet", "verkoopopbrengsten", "inkomsten uit verkochte goederen", "inkomsten uit verleende diensten"],
        "balance": "credit",
        "id": "Revenue",
        "category": "revenue",
        "statement_type": "income_statement"
    },

    # Expenses
    "Expenses": {
        "English": ["cost of sales", "cost of revenue", "direct costs attributable to goods sold", "expenses related to business operations", "rent", "utilities", "salaries", "expense for reduction in value of assets"],
        "Dutch": ["kostprijs van de verkopen", "kosten van de omzet", "rechtstreekse kosten toe te rekenen aan verkochte goederen", "bedrijfskosten", "huur", "nutsvoorzieningen", "salarissen", "kosten voor waardevermindering van activa"],
        "balance": "debit",
        "id": "Expenses",
        "category": "expenses",
        "statement_type": "income_statement"
    },

    # Net Income
    "Net Income": {
        "English": ["net profit", "net earnings", "bottom line", "final profit after all expenses", "operating profit", "operating loss", "pre-tax profit", "pre-tax loss"],
        "Dutch": ["nettowinst", "netto inkomen", "uiteindelijke winst na alle kosten", "bedrijfsresultaat", "exploitatieresultaat", "resultaat voor belasting", "resultaat na belastingen"],
        "balance": "debit",
        "id": "NetIncome",
        "category": "revenue",
        "statement_type": "income_statement"
    },
    
      "Accounts Payable": {
        "English": ["accounts payable", "obligations to suppliers"],
        "Dutch": ["crediteuren", "verplichtingen aan leveranciers"],
        "balance": "credit",
        "id": "AccountsPayable",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Unearned Revenue": {
        "English": ["unearned revenue", "payments received for goods or services not yet delivered"],
        "Dutch": ["ontvangen opbrengsten", "vooruitontvangen betalingen voor nog niet geleverde goederen of diensten"],
        "balance": "credit",
        "id": "UnearnedRevenue",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Short-term Debt": {
        "English": ["short-term debt", "loans and borrowings due within one year"],
        "Dutch": ["korte-termijnschulden", "leningen en kredieten die binnen een jaar verschuldigd zijn"],
        "balance": "credit",
        "id": "ShortTermDebt",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Current Portion of Long-term Debt": {
        "English": ["current portion of long-term debt", "the portion of long-term debt due within the next year"],
        "Dutch": ["kortlopend deel van de langlopende schuld", "deel van de langlopende schuld dat binnen het volgende jaar verschuldigd is"],
        "balance": "credit",
        "id": "CurrentPortionOfLongTermDebt",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Other Accrued Expenses and Liabilities": {
        "English": ["other accrued expenses and liabilities", "expenses incurred but not yet paid"],
        "Dutch": ["overige opgelopen kosten en verplichtingen", "gemaakte kosten maar nog niet betaald"],
        "balance": "credit",
        "id": "OtherAccruedExpensesAndLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Long-term Debt": {
        "English": ["long-term debt", "loans and borrowings not due within the next year"],
        "Dutch": ["langlopende schuld", "leningen en kredieten die niet binnen het volgende jaar verschuldigd zijn"],
        "balance": "credit",
        "id": "LongTermDebt",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Current Receivables": {
        "English": ["current receivables from other legal entities and companies with a participating interest", "receivables from affiliates", "receivables from associated companies", 'current assets receivables trade receivables', 'receivables trade receivables', 'taxes and social security charges'],
        "Dutch": ["vorderingen op andere rechtspersonen en vennootschappen met een deelnemingsbelang", "vorderingen op gelieerde ondernemingen", "vorderingen op deelnemende ondernemingen"],
        "balance": "debit",
        "id": "CurrentReceivablesFromOtherEntities",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    
    "Total of Receivables": {
        "English": ["total of receivables", "aggregate receivables", "sum of receivables"],
        "Dutch": ["totaal vorderingen", "geaggregeerde vorderingen", "som van vorderingen"],
        "balance": "debit",
        "id": "TotalOfReceivables",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    
    "Depreciation of Property, Plant, and Equipment": {
        "English": ["depreciation of property, plant, and equipment", "amortisation of property, plant, and equipment", "depreciation", "amortization of tangible assets", "depreciation of property, plant and equipment"],
        "Dutch": ["afschrijvingen op materiële vaste activa", "afschrijvingen", "amortisatie van materiële vaste activa"],
        "balance": "credit",
        "id": "DepreciationOfPPE",
        "category": "expenses",
        "statement_type": "income_statement"
    },
    "Inventories under Construction": {
        "English": ["inventories under construction", "construction in progress", "work in progress"],
        "Dutch": ["onderhanden werk", "bouw in uitvoering", "werk in uitvoering"],
        "balance": "debit",
        "id": "InventoriesUnderConstruction",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Finished and Trade Goods": {
        "English": ["finished and trade goods", "finished goods", "merchandise", "trading stock"],
        "Dutch": ["gereed product en handelsgoederen", "afgewerkte producten", "handelswaren", "handelsvoorraad"],
        "balance": "debit",
        "id": "FinishedAndTradeGoods",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Total of Inventories": {
        "English": ["total of inventories", "total inventories", "aggregate inventories"],
        "Dutch": ["totaal voorraden", "totale voorraden", "geaggregeerde voorraden"],
        "balance": "debit",
        "id": "TotalOfInventories",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Receivables Trade Receivables": {
        "English": ["receivables trade receivables", "trade receivables", "accounts receivable", "debtors"],
        "Dutch": ["handelsvorderingen", "vorderingen uit handel", "debiteuren", "rekeningen te ontvangen"],
        "balance": "debit",
        "id": "ReceivablesTradeReceivables",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Taxes and Social Security Charges": {
        "English": ["taxes and social security charges", "tax receivables", "government receivables"],
        "Dutch": ["belastingen en sociale zekerheidsbijdragen", "belastingvorderingen", "overheidsvorderingen"],
        "balance": "debit",
        "id": "TaxesAndSocialSecurityCharges",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "not applicable": {
        "English": ["not applicable", "the text does not mention any category name", " i cannot extract the requested data"],
        "Dutch" : ["not applicable", " the text does not mention any category name", " i cannot extract the requested data"],
        "balance": "none",
        "id": "none",
        "category": "none",
        "statement_type": "none"
    },
    "Inventories Under Construction": {
        "English": ["inventories under construction"],
        "Dutch": ["onderhanden werk"],
        "balance": "debit",
        "id": "InventoriesUnderConstruction",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Finished and Trade Goods": {
        "English": ["finished goods", "trade goods"],
        "Dutch": ["gereed product", "handelsgoederen"],
        "balance": "debit",
        "id": "FinishedAndTradeGoods",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Total of Inventories": {
        "English": ["total of inventories"],
        "Dutch": ["totaal voorraden"],
        "balance": "debit",
        "id": "TotalOfInventories",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Prepayments and Accrued Income": {
        "English": ["prepayments", "accrued income"],
        "Dutch": ["vooruitbetalingen", "overlopende activa"],
        "balance": "debit",
        "id": "PrepaymentsAndAccruedIncome",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Total of Current Assets": {
        "English": ["total of current assets"],
        "Dutch": ["totaal vlottende activa"],
        "balance": "debit",
        "id": "TotalOfCurrentAssets",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Total of Assets": {
        "English": ["total of assets"],
        "Dutch": ["totaal activa"],
        "balance": "debit",
        "id": "TotalOfAssets",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Group Equity": {
        "English": ["group equity"],
        "Dutch": ["groepsvermogen"],
        "balance": "credit",
        "id": "GroupEquity",
        "category": "equity",
        "statement_type": "balance_sheet"
    },
    "Non-Current Liabilities": {
        "English": ["non-current liabilities", "debentures", "mortgage bonds", "other loans", "debentures", "mortgage bonds", "other loans"],
        "Dutch": ["niet-vlottende passiva", "obligaties", "hypotheekobligaties", "overige leningen"],
        "balance": "credit",
        "id": "NonCurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Total of Non-Current Liabilities": {
        "English": ["total of non-current liabilities"],
        "Dutch": ["totaal niet-vlottende passiva"],
        "balance": "credit",
        "id": "TotalOfNonCurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Total of Current Liabilities": {
        "English": ["total of current liabilities"],
        "Dutch": ["totaal kortlopende passiva"],
        "balance": "credit",
        "id": "TotalOfCurrentLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Total of Equity and Liabilities": {
        "English": ["total of equity and liabilities"],
        "Dutch": ["totaal eigen vermogen en passiva"],
        "balance": "credit",
        "id": "TotalOfEquityAndLiabilities",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Severance Payments": {
        "English": ["severance payments"],
        "Dutch": ["ontslagvergoedingen"],
        "balance": "debit",
        "id": "SeverancePayments",
        "category": "expenses",
        "statement_type": "income_statement"
    },
    "Total of Expenses of Employee Benefits": {
        "English": ["total of expenses of employee benefits"],
        "Dutch": ["totaal personeelskosten"],
        "balance": "debit",
        "id": "TotalOfExpensesOfEmployeeBenefits",
        "category": "expenses",
        "statement_type": "income_statement"
    },
       "Income Tax Expense": {
        "English": ["income tax expense"],
        "Dutch": ["inkomstenbelasting"],
        "balance": "debit",
        "id": "IncomeTaxExpense",
        "category": "expenses",
        "statement_type": "income_statement"
    },
    "Share in Results of Participating Interests": {
        "English": ["share in results of participating interests"],
        "Dutch": ["deel in resultaten van deelnemende belangen"],
        "balance": "credit",
        "id": "ShareInResultsOfParticipatingInterests",
        "category": "revenue",
        "statement_type": "income_statement"
    },
    "Operating Result": {
        "English": ["operating result"],
        "Dutch": ["bedrijfsresultaat"],
        "balance": "either",
        "id": "OperatingResult",
        "category": "result",
        "statement_type": "income_statement"
    },
    "Other Interest Income and Related Income": {
        "English": ["other interest income and related income", "revenues from other receivables", "other revenues from other receivables"],
        "Dutch": ["overige rentebaten en soortgelijke opbrengsten", "opbrengsten uit andere vorderingen", "andere opbrengsten uit andere vorderingen"],
        "balance": "credit",
        "id": "OtherInterestIncomeAndRelatedIncome",
        "category": "revenue",
        "statement_type": "income_statement"
    },
    "Interest Expenses and Related Expenses": {
        "English": ["interest expenses and related expenses", "costs on liabilities", "other interest expenses"],
        "Dutch": ["rente- en soortgelijke kosten", "kosten voor verplichtingen", "overige rentekosten"],
        "balance": "debit",
        "id": "InterestExpensesAndRelatedExpenses",
        "category": "expenses",
        "statement_type": "income_statement"
    },
    "Non Current Assets": {
        "English": ["non-current assets", "other tangible assets", "long-term assets", "fixed assets"],
        "Dutch": ["niet-vlottende activa", "overige materiële activa", "langetermijnactiva", "vaste activa"],
        "balance": "debit",
        "id": "NonCurrentAssets",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Total of Non Current Assets": {
        "English": ["total of non-current assets", "aggregate non-current assets"],
        "Dutch": ["totaal niet-vlottende activa", "totaal langetermijnactiva"],
        "balance": "debit",
        "id": "TotalOfNonCurrentAssets",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Financial Assets": {
        "English": ["financial assets", "investment securities", "held-to-maturity investments"],
        "Dutch": ["financiële activa", "beleggingswaarden", "beleggingen tot einde looptijd"],
        "balance": "debit",
        "id": "FinancialAssets",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Repayment Obligations of Non Current Borrowings": {
        "English": ["repayment obligations of non-current borrowings", "long-term debt repayments"],
        "Dutch": ["aflossingsverplichtingen van niet-vlottende leningen", "afbetalingen op langlopende schulden"],
        "balance": "credit",
        "id": "RepaymentObligationsOfNonCurrentBorrowings",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Accruals and Deferred Income": {
        "English": ["accruals and deferred income", "deferred revenues", "accrued liabilities"],
        "Dutch": ["overlopende passiva en uitgestelde inkomsten", "uitgestelde opbrengsten", "opgelopen verplichtingen"],
        "balance": "credit",
        "id": "AccrualsAndDeferredIncome",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Operating Income": {
        "English": ["other operating income", "total operating income", "business income", "operating revenues", "total operating income net revenue"],
        "Dutch": ["overige bedrijfsopbrengsten", "totaal bedrijfsopbrengsten", "bedrijfsinkomsten", "exploitatieopbrengsten"],
        "balance": "credit",
        "id": "OperatingIncome",
        "category": "revenue",
        "statement_type": "income_statement"
    },
    "Payables": {
        "English": ["payables to banks", "payables relating to taxes and social security contributions", "payables to taxes and social security contributions", "payables to social security contributions", "payables relating to taxes and social security contributions value added tax"],
        "Dutch": ["schulden aan banken", "verplichtingen met betrekking tot belastingen en sociale zekerheidsbijdragen", "btw-verplichtingen"],
        "balance": "credit",
        "id": "Payables",
        "category": "liabilities",
        "statement_type": "balance_sheet"
    },
    "Operating Expenses": {
        "English": ["operating expenses", "expenses of employee benefits wages", "car and transport costs", "office related expenses", "general expenses", "total of other operating expenses", "administrative expenses", "selling expenses"],
        "Dutch": ["bedrijfskosten", "personeelskosten lonen", "auto- en transportkosten", "kantoorkosten", "algemene kosten", "totaal overige bedrijfskosten", "administratieve kosten", "verkoopkosten"],
        "balance": "debit",
        "id": "OperatingExpenses",
        "category": "expenses",
        "statement_type": "income_statement"
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


