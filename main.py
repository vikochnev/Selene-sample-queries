from selene.support.shared import browser
from selene import have, by

browser.open('https://google.com/ncr')
browser.element('[name=q]').type('possums').press_enter()
browser.element(by.id('search')).should(have.text('Opossum - Wikipedia'))