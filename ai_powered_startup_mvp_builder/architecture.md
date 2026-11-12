# System Architecture - Team Request & Live Chat Hub

## Overview
The application follows a lightweight client-server architecture hosted on Val Town. A responsive single-page web client communicates via HTTP/JSON endpoints with serverless Val Town backend handlers, which read from and write to persistent key-value storage (`ValStorage`).

## High-Level System Diagram

```text
+-------------------------------------------------------------------+
|                        Client Browser (UI)                        |
|  +-----------------------------+  +----------------------------+  |
|  |       Navigation Tabs       |  |    Notification System     |  |
|  |     [ Requests | Chat ]     |  | (Toasts & Error Banners)   |  |
|  +--------------+--------------+  +-------------+--------------+  |
|                 |                               ^                 |
|        +--------+--------+                      |                 |
|        v                 v                      |                 |
|  +-----------+    +-------------+               |                 |
|  | Requests  |    |  Chat View  |               |                 |
|  | Form/Feed |    | (User Gate) |               |                 |
|  +-----+-----+    +------+------+               |                 |
+--------|-----------------|----------------------|-----------------+
         |                 |                      |
         | POST / GET      | POST / GET           | JSON Response
         | (JSON)          | (JSON)               | (200 OK / 4xx)
         v                 v                      |
+-------------------------------------------------------------------+
|                 Val Town HTTP Server (API Layer)                  |
|  +-----------------------------+  +----------------------------+  |
|  |     /api/requests Handler   |  |     /api/chat Handler      |  |
|  |  - Input validation         |  |  - Username & text check   |  |
|  |  - Timestamp generation     |  |  - Message list cap (200)  |  |
|  +--------------+--------------+  +-------------+--------------+  |
+-----------------|-------------------------------|-----------------+
                  |                               |
                  v                               v
+-------------------------------------------------------------------+
|                   Persistent Storage (ValStorage)                 |
|  +-----------------------------+  +----------------------------+  |
|  |      requests_store[]       |  |      chat_messages[]       |  |
|  |  (Max 100 Request Records)  |  |  (Max 200 Message Records) |  |
|  +-----------------------------+  +----------------------------+  |
+-------------------------------------------------------------------+
