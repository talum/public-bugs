const add = require('./add')

describe('add', () => {
  test('returns the sum', () => {
    expect(add(5,3)).toEqual(8)
  })
})
