const { convertCoordinates, findSafePlaces, adviceForAlex } = require('../src/savePlaces')

// Please enable Level 1, 2, 3-Tests by replacing xdescribe with describe!
// Do not edit the tests itself!
xdescribe('Spy Places Level 1 - convert coordinates', () => {
  it('no agents return empty array', () => {
    expect(convertCoordinates([])).toEqual([])
  })
  it('one agent casts to array', () => {
    const agents = ['F3']
    expect(convertCoordinates(agents).length).toEqual(agents.length)
    expect(convertCoordinates(agents)).toEqual(expect.arrayContaining([[5,2]]))
  })
  it('some agents casts to array', () => {
    const agents = ['B6', 'C2', 'J7']
    expect(convertCoordinates(agents).length).toEqual(agents.length)
    expect(convertCoordinates(agents)).toEqual(expect.arrayContaining([[1, 5], [2, 1], [9, 6]]))
  })
  it('handle two digits', () => {
    const agents = ['J10']
    expect(convertCoordinates(agents).length).toEqual(agents.length)
    expect(convertCoordinates(agents)).toEqual(expect.arrayContaining([[9, 9]]))
  })
})

xdescribe('Spy Places Level 2 - find save places', () => {
  it('some places are save if agents are some', () => {
    const agents = [[1, 1], [3, 5], [4, 8], [7, 3], [7, 8], [9, 1]]
    expect(findSafePlaces(agents).length).toEqual(3)
    expect(findSafePlaces(agents)).toEqual(expect.arrayContaining([[0, 9], [0, 7], [5, 0]]))
  })
  it('some places are save if agents are some', () => {
    const agents = [[0, 0], [0, 9], [1, 5], [5, 1], [9, 0], [9, 9]]
    expect(findSafePlaces(agents).length).toEqual(3)
    expect(findSafePlaces(agents)).toEqual(expect.arrayContaining([[5, 7], [6, 6], [7, 5]]))
  })
  it('one place is save', () => {
    const agents = [[0, 0]]
    expect(findSafePlaces(agents).length).toEqual(1)
    expect(findSafePlaces(agents)).toEqual(expect.arrayContaining([[9, 9]]))
  })
})

xdescribe('Spy Places Level 3 - find edge cases and give advice to Alex', () => {
  it('should be replaced with a descriptive message', () => {
    const agents = []
    expect(adviceForAlex(agents)).toEqual('The whole city is safe for Alex! :-)')
  })
  it('no place is save if agents are everywhere', () => {
    const agents =
      ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10',
       'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10',
       'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10',
       'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10',
       'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
       'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
       'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
       'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10',
       'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
       'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10']

    expect(adviceForAlex(agents)).toEqual('There are no safe locations for Alex! :-(')
  })

  it('some places are save if agents are some', () => {
    const agents = ['B2', 'D6', 'E9', 'H4', 'H9', 'J2']
    expect(adviceForAlex(agents).length).toEqual(3)
    expect(adviceForAlex(agents)).toEqual(expect.arrayContaining(['A10', 'A8', 'F1']))
  })
  it('some places are save if agents are some', () => {
    const agents = ['B4', 'C4', 'C8', 'E2', 'F10', 'H1', 'J6']
    expect(adviceForAlex(agents).length).toEqual(11)
    expect(adviceForAlex(agents)).toEqual(expect.arrayContaining(['A1', 'A10', 'E6', 'F5', 'F6', 'G4', 'G5', 'G7', 'H8', 'I9', 'J10']))
  })
  it('some places are save if agents are some', () => {
    const agents = ['A1', 'A10', 'B6', 'F2', 'J1', 'J10']
    expect(adviceForAlex(agents).length).toEqual(3)
    expect(adviceForAlex(agents)).toEqual(expect.arrayContaining(['F8', 'G7', 'H6']))
  })
  it('one save place', () => {
    const agents = ['A1']
    expect(adviceForAlex(agents).length).toEqual(1)
    expect(adviceForAlex(agents)).toEqual(expect.arrayContaining(['J10']))
  })
  it('agent outside the city', () => {
    const agents = ['A12']
    expect(adviceForAlex(agents)).toEqual('The whole city is safe for Alex! :-)')
  })
})
