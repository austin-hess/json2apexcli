public without sharing class CS_Individuals {
	public String ID;
	public String firstName;
	public String lastName;
	public String middleName;
	public String suffixName;
	public CS_Address address;
	public String ssn;
	public String dateOfBirth;
	public Integer tinStatus;
	public CS_PreviousAddresses[] previousAddresses;
	public CS_Employers[] employers;
	public CS_PreviousEmployers[] previousEmployers;
	public CS_Identifications[] identifications;
	public CS_Phones[] phones;
	public Boolean isOFACVerified;
	public String spouseID;
	public Boolean isPrimaryOwner;
	public Boolean isCIVDocumentRequired;
	public CS_ATMDebitCard ATMDebitCard;
	public CS_String[] attorneysInFact;
	public Boolean isMinor;
}