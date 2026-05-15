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
| Preconditions | Valid `user-id` is provided. User balance is greater than €1.00. At least one upcoming match is available. |
| Steps | 1. Open the application <br> 2. Select a football match <br> 3. Select one odds option (`1`, `X`, or `2`) <br> 4. Enter valid stake amount (e.g. `10`) <br> 5. Click `Place Bet` |
| Expected Result | Bet is placed successfully. Loading state is shown during processing. Success receipt modal appears showing correct bet details, payout, odds, stake, and timestamp. Balance is reduced by the stake amount. Active selection is cleared after closing receipt. |

---

# TC-002 — Stake Validation Boundary Testing

| Field | Details |
|---|---|
| Priority | Critical |
| Risk Rationale | Stake validation directly impacts financial correctness and business rule enforcement. Boundary defects are high risk in betting systems. |
| Preconditions | Valid match selection exists |
| Steps | 1. Select valid match and outcome <br> 2. Test stake values: empty, `0`, `0.99`, `1.00`, `1.01`, `100`, `100.01`, `10.999`, `abc` <br> 3. Attempt to place bet for each value |
| Expected Result | Invalid values are rejected with clear validation messaging. Only valid numeric values with max 2 decimal places and valid range are accepted. |

---

# TC-003 — Balance Deduction After Successful Bet

| Field | Details |
|---|---|
| Priority | Critical |
| Risk Rationale | Incorrect balance handling may cause inconsistent financial data and loss of user trust. |
| Preconditions | User has known starting balance |
| Steps | 1. Record current balance <br> 2. Select valid match and outcome <br> 3. Enter valid stake <br> 4. Place bet successfully |
| Expected Result | User balance is reduced exactly by the stake amount after successful bet placement. Updated balance is reflected consistently across the UI. |

---

# TC-004 — Potential Payout Consistency Validation

| Field | Details |
|---|---|
| Priority | High |
| Risk Rationale | Incorrect payout calculations can mislead users about expected winnings and create financial trust issues. |
| Preconditions | Valid match selection exists |
| Steps | 1. Select a match and outcome <br> 2. Enter valid stake amount <br> 3. Verify payout displayed in bet slip <br> 4. Place bet successfully <br> 5. Compare payout shown in receipt modal |
| Expected Result | Potential payout shown in success receipt matches the payout previously displayed in the bet slip and follows correct calculation formula (`stake × odds`). |

---

# TC-005 — Date and Odds Filter Validation

| Field | Details |
|---|---|
| Priority | High |
| Risk Rationale | Incorrect filtering behavior may prevent users from finding relevant matches and can create misleading or inconsistent search results. Validation issues in range filters may also negatively impact usability and trust in displayed data. |
| Preconditions | User is on Upcoming Football Matches page |
| Steps | 1. Apply single-day date filters and verify displayed matches <br> 2. Apply valid date range filters and verify results are correctly filtered <br> 3. Apply invalid date ranges and verify validation handling <br> 4. Apply valid odds min/max ranges and verify results are filtered correctly <br> 5. Test multiple invalid odds range combinations (e.g. minimum greater than maximum, unsupported values, empty ranges) |
| Expected Result | Valid date and odds ranges correctly filter displayed matches. Invalid ranges are rejected with clear validation feedback and should not produce misleading or empty result states without explanation. |

---

# TC-006 — Unauthorized API Request Validation

| Field | Details |
|---|---|
| Priority | High |
| Risk Rationale | Missing authentication and user context validation may expose backend functionality to unauthorized requests. |
| Preconditions | API documentation is available |
| Steps | 1. Send `POST /api/place-bet` request without `x-user-id` header <br> 2. Submit valid request payload |
| Expected Result | API rejects the request with `401 Unauthorized`. No bet is created and no balance changes occur. |