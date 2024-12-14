# General coding exercise

## Introduction

A simple tax calculator, designed to recreate a simpler version
of the official Australian Tax calculator website found at:
https://www.ato.gov.au/single-page-applications/calculatorsandtools#STC/questions

Implemented in python for simplicity and coding velocity.

## Goals

- [ ] Cater for 2021-22 and 2020-2021 tax years
- [ ] Implement ATO tax rates and how they work.
- [ ] At least choose a year and an income, report tax estimate

Stretch goals:

- [ ] Maybe report tax rates per FY in a table?
- [ ] Maybe a more involved GUI?
- [ ] Deployment: Can we serve this online
- [ ] Do we want to serve this using Docker etc?
- [ ] Do we care about scalability?

## Considerations

0. My first thought is to just scrape the ATO site, but I think that might be 
against the spirit of the thing :)
1. Input is a FY (a string like `2020-2021`) and an income 
(a number, let's make it a float for now)
2. Output is a float to 2 decimal places. Bonus points for nice 
number formatting like `$21,732.00`
3. Unit tests are good, let's add those
4. The problem statement doesn't mention residency 
considerations or the medicare levy, so let's not add this 
for now

