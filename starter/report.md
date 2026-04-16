Nazaneen Baguaei
Professor Wu
ET721
April 2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

Before I added any new tests, the code coverage was sitting at around 53%. The routes.py file had barely any coverage and a lot of the model functions weren't being tested either. After I went through and completed all the unit tests in test_models.py, test_search.py, and added more API tests in test_api.py, the coverage went up to 87% with 20 tests passing. That's a pretty big jump and it honestly surprised me how much of a difference just writing proper tests made.

## Untested Code: Effects

Honestly, without the tests it was kind of hard to fully understand what the code was doing. I could read through it but I wasn't 100% sure what inputs would break it or what edge cases existed. Testing the API manually would have been really tedious because you'd have to remember to check everything yourself every single time you make a change. Having only a few tests made me feel unsure about the code, like I didn't really know if things were working the way they were supposed to.

## Adding Tests

The way I went about adding tests was by reading through the existing code first and figuring out what each function was supposed to do. Then I wrote tests for the normal cases, the edge cases like empty lists or zero values, and the error cases where bad input should raise an error. One thing I learned is that unit tests and API tests are pretty different. Unit tests are fast and test one small piece of code at a time, while API tests send actual HTTP requests and test whether the whole app is working together. Both are useful but in different ways. Unit tests help you find exactly where a bug is, and API tests make sure everything connects properly end to end.

## Automation

Running coverage automatically was really helpful because it showed me exactly which lines weren't being tested. Instead of guessing what I needed to cover, I could just look at the report and see the specific line numbers that were missing. It made the whole process a lot more efficient and I felt like I actually knew what I was doing rather than just writing random tests and hoping for the best.

## New Features

Having tested code as a baseline made adding new things feel a lot less scary. When the existing tests were all passing, I knew the core functionality was working before I touched anything. If I broke something while adding a new feature, the tests would catch it right away instead of me finding out later in a weird way. That kind of safety net is something I didn't really appreciate before this project but now I totally get why it matters.

## Future

After doing this project I think my biggest takeaway is that writing tests as you go is way better than trying to add them after the fact. It was a little overwhelming at first because there was already a lot of untested code to deal with, but once I got into it the process made sense. Going forward I want to make it a habit to write tests alongside my code so I don't end up in the same situation again.