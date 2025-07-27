import json

with open("/root/pr23_details.json") as f:
    pr = json.load(f)
summary = {
    "title": pr.get("title"),
    "body": pr.get("body"),
    "files_changed": [f["path"] for f in pr.get("files", [])],
    "author": pr.get("author", {}).get("login"),
    "labels": [l["name"] for l in pr.get("labels", [])],
    "assignees": [a["login"] for a in pr.get("assignees", [])],
    "base_branch": pr.get("baseRefName"),
    "head_branch": pr.get("headRefName"),
    "commits": len(pr.get("commits", [])),
    "reviews": pr.get("reviews", []),
    "status_checks": pr.get("statusCheckRollup", []),
}
ci_summary = []
all_passed = True
for check in summary["status_checks"]:
    name = check.get("name")
    status = check.get("status")
    conclusion = check.get("conclusion")
    ci_summary.append(f"{name}: {status} ({conclusion})")
    if conclusion != "SUCCESS":
        all_passed = False
print("PR SUMMARY:", summary)
print("CI/CD SUMMARY:", ci_summary)
print("ALL CHECKS PASSED:", all_passed)
