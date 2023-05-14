import Button from "../UI/Button";

import style from "./Book.module.css"

const Book = props => {
    // console.log(props.book.title);
    // console.log(props.book)
    return (
      <div className={style["book-section"]}>
        <img
          src={"http://127.0.0.1:8000" + props.book.book_cover}
          className={style["book-cover"]}
          alt={props.book.title}
        />
        <div className={style["book-details"]}>
          <p className={style["book-title"]}>{props.book.title}</p>
          <p className={style["book-description"]}>{props.book.description}</p>

          {/* <p className={style["book-publication"]}>{props.book.publication}</p> */}
          <p className={style["book-publish_year"]}>
            Publication Year: {props.book.publish_year}
          </p>

          <p className={style["book-authors"]}>
            Authors:
            {props.book.authors.map((author) => (
              <span className={style["book-authors-name"]}>{author}</span>
            ))}
          </p>
        </div>
        <div className={style["book-actions"]}>
          <p className={style["book-issue_duration"]}>
            Free Book Issue Period: {props.book.issue_duration} Days
          </p>
          <Button className={style["issue-book-btn"]}>
            Issue Book
          </Button>
          <Button className={style["buy-book-btn"]}>
            Buy Book
          </Button>
          <p className={style["book-stock"]}>{props.book.stock} books left</p>
          <p className={style["book-price"]}>{props.book.price}</p>
          <p className={style["book-pdf"]}>{props.book.pdf}</p>
        </div>
      </div>
    );
}

export default Book;