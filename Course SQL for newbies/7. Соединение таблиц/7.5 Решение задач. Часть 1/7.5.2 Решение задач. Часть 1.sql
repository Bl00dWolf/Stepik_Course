SELECT Elements.symbol AS metal, EL1.symbol AS nonmetal
FROM Elements
         CROSS JOIN Elements AS EL1
WHERE Elements.type = 'metal'
  AND EL1.type = 'nonmetal';