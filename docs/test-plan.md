# Test Plan – Single Bet Placement Feature

## Overview

This document covers the prioritized manual test scenarios for the Single Bet Placement feature based on the provided functional specification.

The selected scenarios focus on:
- Critical business flows
- Financial and validation risks
- Boundary conditions
- Data consistency
- API authorization validation

---

# TC-001 — Successful Single Bet Placement

| Field | Details |
|---|---|
| Priority | Critical |
| Risk Rationale | This is the core business flow of the application. Failure prevents users from placing bets and directly impacts revenue and platform trust. |
| Preconditions | Valid `user-id` is provided. At least one upcoming match is available. |
| Steps | 1. Open the application <br> 2. Select a football match <br> 3. Select one odds option (`1`, `X`, or `2`) <br> 4. Enter valid stake amount <br> 5. Click `Place Bet` |
| Expected Result | Bet is placed successfully. Loading state is displayed during processing. Success receipt modal appears containing bet information. Closing the receipt clears the active selection and returns the user to the main flow. |

---

# TC-002 — Stake Validation Boundary Testing

| Field | Details |
|---|---|
| Priority | Critical |
| Risk Rationale | Stake validation directly impacts financial correctness and business rule enforcement. Boundary defects are high risk in betting systems. |
| Preconditions | Valid match selection exists |
| Steps | 1. Select valid match and outcome <br> 2. Test multiple stake boundary and invalid values (empty, zero, negative, over maximum, invalid precision, non-numeric values) <br> 3. Attempt to place bet for each value |
| Expected Result | Invalid values are rejected with clear validation messaging. Only valid numeric values within allowed limits and precision are accepted. |

---

# TC-003 — Balance Update Consistency After Successful Bet Placement

| Field | Details |
|---|---|
| Priority | Critical |
| Risk Rationale | Incorrect balance synchronization may result in inconsistent financial information and reduced user trust. |
| Preconditions | User has known starting balance |
| Steps | 1. Record current displayed balance <br> 2. Place a valid successful bet <br> 3. Observe updated balance in all visible UI locations |
| Expected Result | Displayed balance is updated immediately after successful placement and reflects the deducted stake amount consistently across the UI. |

---

# TC-004 — Potential Payout Calculation and Display Consistency

| Field | Details |
|---|---|
| Priority | High |
| Risk Rationale | Incorrect payout calculations or inconsistent payout display may mislead users about expected winnings. |
| Preconditions | Valid selection exists |
| Steps | 1. Select a match and outcome <br> 2. Enter valid stake amount <br> 3. Observe calculated payout in bet slip <br> 4. Place bet successfully <br> 5. Compare payout values shown in receipt modal and backend response |
| Expected Result | Potential payout values remain consistent across bet slip, receipt modal, and backend response, following the correct payout calculation formula. |

---

# TC-005 — Date and Odds Filter Validation

| Field | Details |
|---|---|
| Priority | High |
| Risk Rationale | Incorrect filtering behavior may prevent users from finding relevant matches and can create misleading or inconsistent search results. |
| Preconditions | User is on Upcoming Football Matches page |
| Steps | 1. Apply single-day date filters and verify displayed matches <br> 2. Apply valid date range filters and verify results are correctly filtered <br> 3. Apply invalid date ranges and verify validation handling <br> 4. Apply valid odds min/max ranges and verify results are filtered correctly <br> 5. Test multiple invalid odds range combinations |
| Expected Result | Valid date and odds ranges correctly filter displayed matches. Invalid ranges are rejected with clear validation feedback and should not produce misleading empty result states without explanation. |

---

# TC-006 — Unauthorized API Request Validation

| Field | Details |
|---|---|
| Priority | High |
| Risk Rationale | Missing authentication and user context validation may expose backend functionality to unauthorized requests. |
| Preconditions | API documentation is available |
| Steps | 1. Send `POST /api/place-bet` request without `x-user-id` header <br> 2. Submit valid request payload |
| Expected Result | API rejects the request with `401 Unauthorized`. No bet is created and no balance changes occur. |