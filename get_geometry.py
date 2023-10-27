import ee


def get_bounds(region_name):
    
    if region_name == 'afghan':
            
        geom = ee.Geometry.Polygon(

            [
              [
                70.27809406204916,
                34.043798365898766
              ],
              [
                70.79994464798666,
                34.043798365898766
              ],
              [
                70.79994464798666,
                34.33233747415387
              ],
              [
                70.27809406204916,
                34.33233747415387
              ],
              [
                70.27809406204916,
                34.043798365898766
              ]
            ], 'EPSG:4326', False
        )

    elif region_name == 'sudan':
    
        geom = ee.Geometry.Polygon(
            
            [
                [
                  [
                    33.09961652873555,
                    14.09063032622901
                  ],
                  [
                    33.6022410404543,
                    14.09063032622901
                  ],
                  [
                    33.6022410404543,
                    14.646707097666118
                  ],
                  [
                    33.09961652873555,
                    14.646707097666118
                  ],
                  [
                    33.09961652873555,
                    14.09063032622901
                  ]
                ]
              ], 'EPSG:4326', False
            )

    elif region_name == 'iran':

        geom = ee.Geometry.Polygon(
            [
            [
              [
                48.556574946261954,
                32.54634289750261
              ],
              [
                48.018244868136954,
                32.54634289750261
              ],
              [
                48.03060448727758,
                32.04485995394506
              ],
              [
                48.46731103024633,
                32.04485995394506
              ],
              [
                48.559321528293204,
                32.08501075292506
              ],
              [
                48.58043587765844,
                32.10827850580867
              ],
              [
                48.59914696774633,
                32.13212180060732
              ],
              [
                48.59708703122289,
                32.424130475331516
              ],
              [
                48.57236779294164,
                32.47280364604964
              ],
              [
                48.556574946261954,
                32.54634289750261
              ]
            ]
          ], 'EPSG:4326', False
        )

    return geom