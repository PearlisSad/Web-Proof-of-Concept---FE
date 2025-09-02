from flask import Blueprint, render_template
from .balatro.Deck import Deck
from .balatro.Card import Card



bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/balatro")
def balatro():
    deck = Deck()
    deck.shuffle()
    hands = deck.showHands()
    
    # Convert hands to a list of dicts for the template
    cards = []
    for card in deck.deck[:8]:  # show 8 cards
        cards.append({
            "rank": card.rank,
            "suit": card.suit,
            "symbol": Card.suits[card.suit]
        })
    
    return render_template("pages/balatro.html", cards=cards)

@bp.route("/balatro/play")
def playHand():
    return

@bp.route("/balatro/discard")
def discardHand():
    return

