public without sharing class CS_Accounts {
	public Integer ID;
	public String number;
	public Integer type;
	public Integer ownershipStructure;
	public Integer ownershipType;
	public String primaryOwnerID;
	public String productCode;
	public String productDescription;
	public CS_String[] owners;
	public Integer rateStructure;
	public Integer rateType;
	public Integer compoundingFrequency;
	public Integer creditingFrequency;
	public Integer interestPaymentMethod;
	public CS_Rates[] rates;
	public Decimal depositAmount;
	public CS_String[] fiduciaries;
	public CS_StatementMailingAddress statementMailingAddress;
	public CS_AuthorizedSigners[] authorizedSigners;
	public CS_String[] beneficiaries;
	public CS_SafeDepositBox safeDepositBox;
	public CS_String[] custodians;
	public CS_String[] successorCustodians;
}