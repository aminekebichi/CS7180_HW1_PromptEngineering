import { DataTable, type Column } from './components/DataTable';
import './App.css';

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
  status: 'active' | 'inactive';
}

const mockUsers: User[] = [
  { id: 1, name: "Alice Johnson", email: "alice@example.com", role: "Admin", status: "active" },
  { id: 2, name: "Bob Smith", email: "bob@example.com", role: "Editor", status: "inactive" },
  { id: 3, name: "Charlie Brown", email: "charlie@example.com", role: "Viewer", status: "active" },
  { id: 4, name: "Diana Prince", email: "diana@example.com", role: "Admin", status: "active" },
  { id: 5, name: "Evan Wright", email: "evan@example.com", role: "Editor", status: "active" },
  { id: 6, name: "Fiona Gallagher", email: "fiona@example.com", role: "Viewer", status: "inactive" },
  { id: 7, name: "George Martin", email: "george@example.com", role: "Editor", status: "active" },
  { id: 8, name: "Hannah Lee", email: "hannah@example.com", role: "Viewer", status: "active" },
  { id: 9, name: "Ian Somerhalder", email: "ian@example.com", role: "Admin", status: "inactive" },
  { id: 10, name: "Jane Doe", email: "jane@example.com", role: "Viewer", status: "active" },
];

const columns: Column<User>[] = [
  { key: 'id', header: 'ID' },
  { key: 'name', header: 'Name' },
  { key: 'email', header: 'Email' },
  { key: 'role', header: 'Role' },
  {
    key: 'status',
    header: 'Status',
    render: (value) => (
      <span className={`px-2 py-1 rounded text-sm ${value === 'active' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
        {String(value)}
      </span>
    )
  },
];

function App() {
  return (
    <div className="container mx-auto p-8">
      <h1 className="text-2xl font-bold mb-6">User Management</h1>
      <DataTable data={mockUsers} columns={columns} />
    </div>
  );
}

export default App;
