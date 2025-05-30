markdown_template = """\
# {filename}

## Overview

Brief description of what this file does and its role within the larger project.

## Key Components

### Modules
- List any MODULES defined in this file.

### Subroutines
- List any SUBROUTINES defined in this file.

### Functions
- List any FUNCTIONS defined in this file.

## Important Variables/Constants

- Describe any critical variables or constants defined in this file that affect its behavior.

## Usage Examples

- If applicable, provide examples or code snippets demonstrating how to use the functions, classes, or modules in this file.

## Dependencies and Interactions

### Internal (other project files)
- List any `USE` statements pointing to other modules within this project.

### External (libraries like BLAS, LAPACK)
- List any `USE` statements pointing to external libraries or note other forms of interaction.
"""

print(markdown_template)
