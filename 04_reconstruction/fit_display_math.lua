-- PDF-only: retain math content and let TeX shrink only equations wider than the line.
function Math(el)
  if FORMAT:match('latex') and el.mathtype == 'DisplayMath' then
    return pandoc.Math('DisplayMath', '\\fitdisplaymath{' .. el.text .. '}')
  end
end
