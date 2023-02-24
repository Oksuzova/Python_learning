|     |                                                                                                                              |        |
|-----|------------------------------------------------------------------------------------------------------------------------------|--------|
| 1.  | **Prompt**                                                                                                                   |        |
| 1.1 | The program asking user “What would you like? (espresso/latte/cappuccino):”                                                  | passed |
| 1.2 | The prompt should show every time action has completed.                                                                      | passed |
| 1.3 | The prompt should show again after making a drink to serve the next customer.                                                | passed |
| 2.  | **User action**                                                                                                              |        |
| 2.1 | Check the user’s input to decide what to do next.                                                                            | passed |
| 2.2 | Ensure that the code stops executing when the user enters 'off'. It should turn off coffe machine                            | passed |
| 2.3 | Ensure that the program shows the current resources values when the user enters 'report'                                     | passed |
| 3.  | **Check resources**                                                                                                          |        |
| 3.1 | Ensure that the program checks if there are enough resources to make the selected drink.                                     | passed |
| 3.2 | Ensure that the program displays an error message if there are not enough resources to make the selected drink.              | passed |
| 4.  | **Process coins**                                                                                                            |        |
| 4.1 | Ensure that the program prompts the user to insert coins when there are sufficient resources to make the selected drink.     | passed |
| 4.2 | Ensure that the program calculates the monetary value of the coins inserted correctly.                                       | passed |
| 4.3 | Ensure that the program checks if the user has inserted enough money to purchase the selected drink.                         | passed |
| 4.4 | Ensure that the program refunds the money if the user has not inserted enough money.                                         | passed |
| 4.5 | Ensure that the program adds the cost of the drink to the machine's profit if the user has inserted enough money.            | passed |
| 4.6 | Ensure that the program offers change if the user has inserted too much money.                                               | passed |
| 5.  | **Make coffee**                                                                                                              |        |
| 5.1 | Ensure that the program deducts the correct amount of resources from the machine's resources when making the selected drink. | passed |
| 5.2 | Ensure that the program displays the correct message when the drink is made successfully.                                    | passed | 
| 6.  | **Negative tests**                                                                                                           |        |
| 5.2 | Ensure that the program displays the error message if the user enters an invalid option when prompted for a drink            | failed |
| 5.2 | Ensure that the program displays the error message if the user enters an invalid option when inserted the coins              | failed |