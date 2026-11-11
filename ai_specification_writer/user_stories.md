# User Stories

### User Story 1
As a passenger, I want to search for available rides by origin and destination so that I can find a convenient route to work.

**Acceptance Criteria**:
- User enters pickup location, drop-off location, and desired departure time.
- System displays matching routes filtered within a 5 km radius of origin/destination.
- Each search result displays driver profile summary, departure time, and total cost.

**Priority**: MVP

---

### User Story 2
As a driver, I want to post my daily commuting route and schedule so that passengers can request to join my trip.

**Acceptance Criteria**:
- Driver specifies recurring or one-time start location, end location, route line, departure time, and available seats.
- System validates route path and estimates fuel/toll cost per seat.
- Trip appears immediately in passenger search queries.

**Priority**: MVP

---

### User Story 3
As a passenger, I want to request a seat on a driver's route so that I can lock in my travel plans.

**Acceptance Criteria**:
- Passenger selects an available ride and clicks "Request Seat".
- Driver receives a real-time notification with passenger profile and rating.
- Status changes to "Confirmed" once driver accepts or auto-approves.

**Priority**: MVP

---

### User Story 4
As a user, I want to verify my identity via government ID and phone number so that all platform members feel safe sharing rides.

**Acceptance Criteria**:
- User uploads official photo ID and completes phone SMS verification.
- System updates profile status to "Verified" upon successful check.
- Unverified users are restricted from booking or driver posting.

**Priority**: MVP

---

### User Story 5
As a passenger, I want to pay for my ride automatically within the app so that I do not need to carry cash or handle manual payments.

**Acceptance Criteria**:
- System holds fare payment upon booking confirmation.
- Fare is transferred to the driver upon successful trip completion code entry.
- Digital receipt is emailed to the passenger immediately after the trip ends.

**Priority**: MVP

---

### User Story 6
As a driver or passenger, I want to rate and review my co-travelers after a trip so that the community remains trustworthy.

**Acceptance Criteria**:
- Both driver and passenger receive a post-trip evaluation prompt (1-5 star scale + optional comments).
- Reviews are locked until both parties submit or 48 hours pass.
- Average star rating updates on user public profiles.

**Priority**: High

---

### User Story 7
As a user, I want to message my matched driver/passenger inside the app so that we can coordinate exact pickup points safely.

**Acceptance Criteria**:
- Chat interface becomes active only after a ride request is confirmed.
- Real-time push notifications alert users of new messages.
- Personal phone numbers and emails remain masked.

**Priority**: High

---

### User Story 8
As a passenger, I want to track the driver's location in real time on a map so that I know exactly when they will arrive at the pickup spot.

**Acceptance Criteria**:
- Map updates driver GPS marker position every 5–10 seconds once trip status is "En Route".
- App displays Estimated Time of Arrival (ETA) to pickup point.
- Passenger receives a push alert when the driver is within 200 meters.

**Priority**: Medium

---

### User Story 9
As a user, I want to view my environmental impact dashboard so that I can track how much carbon and money I have saved.

**Acceptance Criteria**:
- Dashboard calculates total distance shared, estimated $ saved, and total $CO_2$ offset in kilograms.
- User can toggle views between weekly, monthly, and lifetime stats.
- Social share button generates a graphic card of personal sustainability impact.

**Priority**: Medium

---

### User Story 10
As a passenger, I want to trigger an emergency SOS alert during an active trip so that my live location is sent to authorities and trusted contacts.

**Acceptance Criteria**:
- Prominent "SOS" button is accessible on active trip screen.
- Pressing SOS broadcasts live GPS coordinates to pre-selected emergency contacts.
- In-app support team is automatically alerted to initiate emergency protocols.

**Priority**: Low
