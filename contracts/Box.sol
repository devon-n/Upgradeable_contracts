// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Box {

    uint256 private value; // Init value

    event ValueChanged(uint256 newValue); // Create event to emit when value changes 

    function store(uint256 newValue) public { // Set the value
        value = newValue;
        emit ValueChanged(newValue);
    }

    function retrieve() public view returns (uint256) { // Get the value
        return value;
    }
}