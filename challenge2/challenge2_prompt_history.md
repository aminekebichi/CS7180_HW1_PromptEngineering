# Prompt History - Challenge 2

1.  Let's move onto challenge 2. Let's create the necessary boiler plate code for a React project that features a sortable/filterable data table with pagination.

    The data table must have the following features:
    - Sortable columns (click to sort)
    - Filter by text input
    - Pagination (configurable page size)
    - Proper TypeScript types

    **Generated Code (v1 - Build Failed):**
    ```tsx
    // src/App.tsx
    import React, { useMemo } from 'react';
    import { DataTable, Column } from './components/DataTable'; // <--- Error here
    
    interface User {
      id: number;
      name: string;
      email: string;
      role: string;
      status: 'active' | 'inactive';
    }

    // ... (rest of App component)
    ```

2.  Let's refine the prompt to ensure compatibility with modern TypeScript bundler settings.

    Let's create the necessary boiler plate code for a React project that features a sortable/filterable data table with pagination.
    The data table must have the following features:
    - Sortable columns (click to sort)
    - Filter by text input
    - Pagination (configurable page size)
    - Proper TypeScript types
    
    **Ensure that when importing types (like interfaces), you use the `import type` syntax to treat them as type-only imports. This is required to be compatible with `verbatimModuleSyntax` which is often enabled in modern Vite configurations.**

    **Generated Code (v2 - Build Passed):**
    ```tsx
    // src/App.tsx
    import React, { useMemo } from 'react';
    import { DataTable, type Column } from './components/DataTable'; // <--- Fixed
    
    interface User {
      id: number;
      name: string;
      email: string;
      role: string;
      status: 'active' | 'inactive';
    }

    const columns: Column<User>[] = [
      { key: 'id', label: 'ID', sortable: true },
      { key: 'name', label: 'Name', sortable: true },
      { key: 'email', label: 'Email', sortable: true },
      { key: 'role', label: 'Role', sortable: true },
      { key: 'status', label: 'Status', sortable: true },
    ];

    // ...
    ```
