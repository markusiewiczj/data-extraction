financial_ledger = {
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
        "English": ["prepaid expenses", "costs paid in advance", "accrued income"],
        "Dutch": ["vooruitbetaalde kosten", "overlopende activa"],
        "balance": "debit",
        "id": "PrepaidExpenses",
        "category": "assets",
        "statement_type": "balance_sheet"
    },
    "Property, Plant, and Equipment": {
        "English": ["property, plant, and equipment", "PPE", "fixed assets", "buildings", "machinery", "long-term assets", "physical assets", "tangible fixed assets"],
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
        "English": ["long-term liabilities", "non-current liabilities", "debentures", "mortgage bonds", "long-term loans", "loans not due within the next year"],
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
        "English": ["net profit", "net earnings", "bottom line", "final profit after all expenses", "operating profit", "operating loss", "pre-tax profit", "pre-tax loss", "result after tax"],
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
 }


def get_terms(term, language):
    """
    Retrieve the synonyms and translations for a given term and language.
    
    :param term: The financial term to look up (e.g., "Revenue")
    :param language: The language for synonyms and translations ("English" or "Dutch")
    :return: A list of terms in the specified language
    """
    return financial_ledger.get(term, {}).get(language, [])


