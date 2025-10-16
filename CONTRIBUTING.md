## Our Contribution Process (Please Read!)

To ensure a fair and organized process for everyone, we follow a "First-Come, First-Served" system.

1.  **Claim an Issue:** Find an issue you want to work on and leave a comment asking to be assigned (e.g., "I'll take this one!" or "Please assign this to me").
2.  **Wait for Assignment:** Please wait for a maintainer to assign the issue to you before you start working. This prevents multiple people from working on the same thing. We will assign it to the first person who commented.
3.  **Submit a Pull Request:** Once you are assigned, you have **3 days** to submit a pull request. If there's no activity after 3 days, the issue will be un-assigned and become available for someone else to claim.
4.  **Link Your PR:** When you create your pull request, please link it to the issue you are solving.

Pull requests submitted for issues that were not claimed or were assigned to someone else will be closed.

## Step-by-Step Contribution Workflow

1.  **Find an Issue: ** Please look through the existing issues and find one you'd like to work on. If you have a new idea, feel free to open a new issue first. Comment on the issue to let us know you're working on it!

2.  **Fork the Repository:** Click the "Fork" button in the top-right corner of the page. This creates a copy of the repository in your own GitHub account.

3.  **Clone Your Fork:** Open your terminal and clone your forked repository:
    ```bash
    git clone [https://github.com/YOUR-USERNAME/Algo-DS-Hub-for-Hacktoberfest.git](https://github.com/YOUR-USERNAME/Algo-DS-Hub-for-Hacktoberfest.git)
    ```
    Pro-Tip: After you clone your fork, it's a great practice to configure a remote that points back to our main repository. This allows you to keep your main branch in sync with the project. You can do this with the command:
    ```bash
    git remote add upstream https://github.com/uptouplaksh/Algo-DS-Hub-for-Hacktoberfest.git
    ```

4.  **Create a New Branch:** A dedicated branch for your feature is essential.
    ```bash
    git checkout -b your-branch-name
    # Example: git checkout -b add-python-binary-search
    ```

5.  **Add Your Code:**
    * Navigate to the correct directory based on our folder structure.
    * Create your file (e.g., `binary_search.py`).
    * Write your code. **Remember to add comments explaining the logic and the Time & Space Complexity.**

    ### Using Templates

    We provide boilerplate template files for each language in the `templates/` folder. 
    Contributors are encouraged to use these templates as a starting point to ensure their code is properly formatted and includes docstrings/comments.

    Available templates:

    - Python: `templates/template.py`
    - Java: `templates/template.java`
    - JavaScript: `templates/template.js`
    - C++: `templates/template.cpp`


6.  **Commit Your Changes:** Make a clear and descriptive commit message.
    ```bash
    git add.
    git commit -m "feat: Add Binary Search algorithm in Python"
    ```

7.  **Push to Your Fork:** Push your changes to your forked repository.
    ```bash
    git push origin your-branch-name
    ```

8.  **Open a Pull Request (PR):**
    * Go to the original repository on GitHub.
    * You will see a prompt to create a Pull Request from your new branch. Click it.
    * Use a clear title (e.g., "Feat: Add Binary Search in Python").
    * In the description, link to the issue you are solving by writing `Closes #issue-number`.
    * Submit the PR!

## Description

A brief, one or two-sentence summary of the changes you've made.

## Changes Made

A bulleted list of the specific changes. For example:
1. Added a new file: algorithms/searching/binary_search/python/binary_search.py
2. Implemented the Binary Search algorithm.
3. Included Time and Space Complexity analysis.

## Related Issue

Please link the issue that this PR is solving. For example:
Closes #17

## Review Process

Please note that the project maintainer (@YourUsername) will be automatically added as a reviewer to all pull requests. We will do our best to review your contribution within 48 hours. Thank you for your patience!

## Troubleshooting Failing Checks

**"Q: I submitted a PR, but one of the automated checks failed with a red 'X'. What should I do?"**

**A:** Don't worry! This can sometimes happen due to GitHub's security settings for repositories, and it's usually not a problem with your code.

Here's what to do:

1. **Don't panic.** This is a common issue, and it will not block your contribution from being merged if the code is good.  
2. **Leave a comment.** Please leave a comment on your pull request and tag the maintainer (`@uptouplaksh`) to let them know. For example:  
   > "@uptouplaksh The `auto-labeler` check failed. Can you please take a look?"  
3. **Wait for the maintainer.** The maintainer can often fix the issue by manually re-running the job or by applying the labels themselves.

As long as your code is high-quality and follows our guidelines, a failing automated check will not prevent your contribution from being accepted.

