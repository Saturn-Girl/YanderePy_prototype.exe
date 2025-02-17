#include <iostream>
#include "Initialization.hpp" // Including the initialization header

int main() {
    // Call initialization functions
    initializePyOpenGL();
    initializePygame();
    initializeCustom();  // Call user-defined function for custom initialization

    // Other code logic
    std::cout << "All systems initialized!" << std::endl;
    
    return 0;
}
