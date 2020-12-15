public without sharing class CS_Accounts {
	public Integer ID;
	public String number_x;
	public Integer type;
	public Integer ownershipStructure;
	public Integer ownershipType;
	public String primaryOwnerID;
	public String productCode;
	public String productDescription;
	public String[] owners;
	public Integer rateStructure;
	public Integer rateType;
	public Integer compoundingFrequency;
	public Integer creditingFrequency;
	public Integer interestPaymentMethod;
	public CS_Rates[] rates;
	public Decimal depositAmount;
	public String[] fiduciaries;
	public CS_StatementMailingAddress statementMailingAddress;
	public CS_AuthorizedSigners[] authorizedSigners;
	public String[] beneficiaries;
	public CS_SafeDepositBox safeDepositBox;
	public String[] custodians;
	public String[] successorCustodians;
}