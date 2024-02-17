# postmortem
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)
## Issue Summary

- Duration: The outage occurred from 10:00 AM to 12:00 PM on February 5, 2024 (UTC).
- Impact: The service impacted was the company's e-commerce platform, which experienced complete downtime during the outage. Users attempting to access the platform encountered error messages or unresponsive pages. Approximately 75% of the users were affected.
- Root Cause: The root cause of the outage was identified as a misconfiguration in the load balancer settings, leading to an overload on the database servers and subsequent service disruption.


## Timeline

- 10:00 AM: The issue was detected when monitoring alerts indicated a sudden increase in server response times.
- 10:05 AM: Engineers noticed multiple error reports from users attempting to access the e-commerce platform.
- 10:10 AM: Initial investigation focused on the database servers due to high CPU and memory usage.
- 10:30 AM: Assumption was made that a database query bottleneck was causing the slowdown.
- 10:45 AM: Misleading investigation paths included optimizing database queries and increasing server capacity.
- 11:00 AM: Incident was escalated to the DevOps team for further investigation.
- 11:30 AM: DevOps team identified the misconfiguration in the load balancer settings as the root cause.
- 12:00 PM: Incident was resolved by correcting the load balancer configuration and restarting affected services.

## Root Cause and Resolution

- Root Cause: The misconfiguration in the load balancer settings caused an imbalance in traffic distribution, leading to an overload on specific database servers.
- Resolution: The load balancer configuration was corrected to evenly distribute traffic among all database servers. Additionally, database connection pooling was implemented to optimize resource utilization during peak loads.

## Corrective and Preventative Measures

### Improvements/Fixes:

- Implement automated load balancer health checks to detect misconfigurations.
- Enhance monitoring and alerting systems to provide early detection of abnormal server behavior.
- Conduct regular load testing and capacity planning to anticipate and mitigate potential issues.
- Establish clear communication channels and escalation procedures to streamline incident response.

### Tasks to Address the Issue:

- Update load balancer configuration to evenly distribute traffic across database servers. (e.g., adjust weights, configure health checks)
- Implement database connection pooling to optimize resource utilization and mitigate overload risks.
- Enhance monitoring system to include load balancer metrics and alerts for misconfigurations.
- Conduct a post-incident review to analyze response procedures and identify areas for improvement.
- Update incident response documentation and conduct team training sessions to ensure readiness for future incidents.