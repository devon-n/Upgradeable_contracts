// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BoxV2 {
    uint256 private value; // Set private value

    event ValueChanged(uint256 newValue); // Event to emit when values changes

    function store(uint256 newValue) public { // Setter function
        value = newValue;
        emit ValueChanged(newValue);
    }

    function retrieve() public view returns (uint256) { // Getter function
        return value;
    }

    function increment() public { // Increment value by one
        value++;
        emit ValueChanged(value);
    }
}