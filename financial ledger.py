financial_ledger = {
    # Assets
    "Cash and Cash Equivalents": {
        "English": ["cash and cash equivalents", "cash", "cash on hand", "liquid assets", "treasury bills", "certificates of deposit", "undeposited receipts", "money market funds"],
        "Dutch": ["contanten en kasequivalenten", "contanten", "liquide middelen", "kasgeld", "schatkistbiljetten", "certificaten van deposito", "niet-gedeponeerde ontvangsten", "geldmarktfondsen"]
    },
    "Marketable Securities": {
        "English": ["marketable securities", "commercial paper", "treasury notes", "money market instruments"],
        "Dutch": ["verhandelbare effecten", "handelspapier", "schatkistpromessen", "geldmarktinstrumenten"]
    },
    "Accounts Receivable": {
        "English": ["accounts receivable", "trade receivables", "debtor's balance", "amounts owed by customers", "money owed by customers"],
        "Dutch": ["debiteuren", "handelsvorderingen", "vorderingen", "door klanten verschuldigd geld"]
    },
    "Inventories": {
        "English": ["inventories", "stock", "goods", "merchandise", "finished goods", "work in progress", "raw materials"],
        "Dutch": ["voorraden", "voorraad", "inventaris", "goederenvoorraad", "gereed product", "onderhanden werk", "grondstoffen"]
    },
    "Prepaid Expenses": {
        "English": ["prepaid expenses", "costs paid in advance", "accrued income"],
        "Dutch": ["vooruitbetaalde kosten", "overlopende activa"]
    },
    "Property, Plant, and Equipment": {
        "English": ["property, plant, and equipment", "PPE", "fixed assets", "buildings", "machinery", "long-term assets", "physical assets", "tangible fixed assets"],
        "Dutch": ["materiële vaste activa", "vaste activa", "gebouwen", "machines", "langetermijnactiva", "tastbare vaste activa"]
    },
    "Intangible Assets": {
        "English": ["intangible assets", "goodwill", "patents", "trademarks", "copyrights"],
        "Dutch": ["immateriële activa", "goodwill", "patenten", "handelsmerken", "auteursrechten"]
    },

  # Liabilities
    "Current Liabilities": {
        "English": ["short-term liabilities", "current liabilities", "trade creditors", "payments received for not yet delivered services", "loans due within one year", "portion of long-term debt due within next year", "expenses incurred but not yet paid"],
        "Dutch": ["kortlopende verplichtingen", "actuele verplichtingen", "handelscrediteuren", "ontvangen betalingen voor nog niet geleverde diensten", "leningen die binnen een jaar verschuldigd zijn", "deel van langlopende schuld dat binnen het volgende jaar verschuldigd is", "gemaakte kosten maar nog niet betaald"]
    },
    "Long-term Liabilities": {
        "English": ["long-term liabilities", "non-current liabilities", "debentures", "mortgage bonds", "long-term loans", "loans not due within the next year"],
        "Dutch": ["langlopende verplichtingen", "niet-actuele verplichtingen", "obligaties", "hypothecaire obligaties", "overige leningen", "leningen die niet binnen het volgende jaar verschuldigd zijn"]
    },
    
    # Shareholders' Equity
    "Shareholder's Equity": {
        "English": ["stockholder's equity", "owners' equity", "shareholders' funds", "money received from investors", "cumulative earnings not distributed"],
        "Dutch": ["eigen vermogen", "aandeelhouderskapitaal", "van investeerders ontvangen geld", "cumulatieve winsten niet uitgekeerd"]
    },

    # Income Statement Items
    "Revenue": {
        "English": ["sales", "income", "turnover", "sales revenue", "net sales", "income from goods sold", "income from services provided"],
        "Dutch": ["omzet", "inkomsten", "opbrengsten", "netto-omzet", "verkoopopbrengsten", "inkomsten uit verkochte goederen", "inkomsten uit verleende diensten"]
    },
    "Expenses": {
        "English": ["cost of sales", "cost of revenue", "direct costs attributable to goods sold", "expenses related to business operations", "rent", "utilities", "salaries", "expense for reduction in value of assets"],
        "Dutch": ["kostprijs van de verkopen", "kosten van de omzet", "rechtstreekse kosten toe te rekenen aan verkochte goederen", "bedrijfskosten", "huur", "nutsvoorzieningen", "salarissen", "kosten voor waardevermindering van activa"]
    },
    "Net Income": {
        "English": ["net profit", "net earnings", "bottom line", "final profit after all expenses", "operating profit", "operating loss", "pre-tax profit", "pre-tax loss", "result after tax"],
        "Dutch": ["nettowinst", "netto inkomen", "uiteindelijke winst na alle kosten", "bedrijfsresultaat", "exploitatieresultaat", "resultaat voor belasting", "resultaat na belastingen"]
    } ,
    "Accounts Payable": {
        "English": ["accounts payable", "obligations to suppliers"],
        "Dutch": ["crediteuren", "verplichtingen aan leveranciers"]
    },
    "Unearned Revenue": {
        "English": ["unearned revenue", "payments received for goods or services not yet delivered"],
        "Dutch": ["ontvangen opbrengsten", "vooruitontvangen betalingen voor nog niet geleverde goederen of diensten"]
    },
    "Short-term Debt": {
        "English": ["short-term debt", "loans and borrowings due within one year"],
        "Dutch": ["korte-termijnschulden", "leningen en kredieten die binnen een jaar verschuldigd zijn"]
    },
    "Current Portion of Long-term Debt": {
        "English": ["current portion of long-term debt", "the portion of long-term debt due within the next year"],
        "Dutch": ["kortlopend deel van de langlopende schuld", "deel van de langlopende schuld dat binnen het volgende jaar verschuldigd is"]
    },
    "Other Accrued Expenses and Liabilities": {
        "English": ["other accrued expenses and liabilities", "expenses incurred but not yet paid"],
        "Dutch": ["overige opgelopen kosten en verplichtingen", "gemaakte kosten maar nog niet betaald"]
    },
    "Long-term Debt": {
        "English": ["long-term debt", "loans and borrowings not due within the next year"],
        "Dutch": ["langlopende schuld", "leningen en kredieten die niet binnen het volgende jaar verschuldigd zijn"]
    }
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

# Example usage
print("English synonyms for 'Revenue':", get_terms("Revenue", "English"))
print("Dutch translations for 'Cash and Cash Equivalents':", get_terms("Cash and Cash Equivalents", "Dutch"))
