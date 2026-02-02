import React, { useState, useMemo } from 'react';

export interface Column<T> {
    key: keyof T;
    header: string;
    render?: (value: T[keyof T], item: T) => React.ReactNode;
}

interface DataTableProps<T> {
    data: T[];
    columns: Column<T>[];
    initialPageSize?: number;
}

export function DataTable<T extends Record<string, any>>({
    data,
    columns,
    initialPageSize = 5
}: DataTableProps<T>) {
    const [sortKey, setSortKey] = useState<keyof T | null>(null);
    const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');
    const [filterText, setFilterText] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [pageSize, setPageSize] = useState(initialPageSize);

    // Handle Sorting
    const handleSort = (key: keyof T) => {
        if (sortKey === key) {
            setSortDirection(prev => prev === 'asc' ? 'desc' : 'asc');
        } else {
            setSortKey(key);
            setSortDirection('asc');
        }
    };

    // Filter Data
    const filteredData = useMemo(() => {
        if (!filterText) return data;
        return data.filter(item =>
            Object.values(item).some(val =>
                String(val).toLowerCase().includes(filterText.toLowerCase())
            )
        );
    }, [data, filterText]);

    // Sort Data
    const sortedData = useMemo(() => {
        if (!sortKey) return filteredData;

        return [...filteredData].sort((a, b) => {
            const aVal = a[sortKey];
            const bVal = b[sortKey];

            if (aVal < bVal) return sortDirection === 'asc' ? -1 : 1;
            if (aVal > bVal) return sortDirection === 'asc' ? 1 : -1;
            return 0;
        });
    }, [filteredData, sortKey, sortDirection]);

    // Paginate Data
    const totalPages = Math.ceil(sortedData.length / pageSize);
    const paginatedData = useMemo(() => {
        const start = (currentPage - 1) * pageSize;
        return sortedData.slice(start, start + pageSize);
    }, [sortedData, currentPage, pageSize]);

    return (
        <div className="p-4 border rounded shadow-sm">
            <div className="mb-4 flex gap-4">
                <input
                    type="text"
                    placeholder="Filter..."
                    value={filterText}
                    onChange={e => {
                        setFilterText(e.target.value);
                        setCurrentPage(1); // Reset to page 1 on filter
                    }}
                    className="p-2 border rounded"
                />
                <select
                    value={pageSize}
                    onChange={e => {
                        setPageSize(Number(e.target.value));
                        setCurrentPage(1);
                    }}
                    className="p-2 border rounded"
                >
                    <option value={5}>5 per page</option>
                    <option value={10}>10 per page</option>
                    <option value={20}>20 per page</option>
                </select>
            </div>

            <table className="w-full text-left border-collapse">
                <thead>
                    <tr className="bg-gray-100 border-b">
                        {columns.map(col => (
                            <th
                                key={String(col.key)}
                                onClick={() => handleSort(col.key)}
                                className="p-3 cursor-pointer hover:bg-gray-200 select-none"
                            >
                                {col.header}
                                {sortKey === col.key && (sortDirection === 'asc' ? ' ▲' : ' ▼')}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {paginatedData.map((row, i) => (
                        <tr key={i} className="border-b hover:bg-gray-50">
                            {columns.map(col => (
                                <td key={String(col.key)} className="p-3">
                                    {col.render ? col.render(row[col.key], row) : String(row[col.key])}
                                </td>
                            ))}
                        </tr>
                    ))}
                    {paginatedData.length === 0 && (
                        <tr>
                            <td colSpan={columns.length} className="p-4 text-center text-gray-500">
                                No matching records found.
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>

            <div className="mt-4 flex justify-between items-center">
                <button
                    onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
                    disabled={currentPage === 1}
                    className="px-3 py-1 border rounded disabled:opacity-50"
                >
                    Previous
                </button>
                <span>Page {currentPage} of {totalPages || 1}</span>
                <button
                    onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
                    disabled={currentPage === totalPages || totalPages === 0}
                    className="px-3 py-1 border rounded disabled:opacity-50"
                >
                    Next
                </button>
            </div>
        </div>
    );
}
