import React from 'react';
import Book from './components/books/Book'

function App() {
  const [books, setBooks] = React.useState([])
  
  // const fetchBooks = 

  React.useEffect(() => {
    async function fetchBooks(){
      const response = await fetch("http://192.168.1.10:8000/books/");
      const data = await response.json()
      setBooks(data);
    }
    fetchBooks();
  }, [])

  return (
    <div className="App">
      {books.map( book => <Book book={book} key={book.id} /> )}
    </div>
  );
}

export default App;
