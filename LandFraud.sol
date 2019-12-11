pragma solidity ^0.4.21;

contract LandFraud {
    
    string private supplier;
    string private customer;
    
    string private property;
    
    function LandFraud() public {}
    
    function addContract(string _supplier, string _customer, string _property) public {
        supplier = _supplier;
        customer = _customer;
        property = _property;
    }
    
    function getSupplier() view public returns (string) {
        return supplier;
    }
    function getCustomer() view public returns (string) {
        return customer;
    }
    function getProperty() view public returns (string) {
        return property;
    }
}
