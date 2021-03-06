import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0E6AFDB7-61EA-E811-9C9E-D4AE529D9537.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/143733A2-73EA-E811-8E38-001E675A4759.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/14E0647B-92EA-E811-A1B3-001E67DDC119.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/16A5F4C7-5DEA-E811-A868-001E67DDC88A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1A31331B-91EA-E811-A015-001E67E6920C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1C19497F-8CEA-E811-A00F-001E67A3FDF8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/22201FBA-91EA-E811-81F6-001E67DFF4F6.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/24200952-86EA-E811-86E1-001E67A40604.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/30066654-5DEA-E811-9304-D4AE529D9537.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/3208364F-70EA-E811-90C6-001E67A42026.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/32750758-88EA-E811-B436-A4BF0102A5F4.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/3CE283BA-69EA-E811-BDBE-001517FB1990.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/4AECE994-89EA-E811-B70C-001E675A58D9.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/50625C53-91EA-E811-AE48-001E67DDC051.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/58024A9C-5DEA-E811-B23A-001E67DDBEDA.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/6A6FDC40-89EA-E811-BC0D-001E67E5A39A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/6CA81381-86EA-E811-955B-001E675A622F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/70D0CC41-8BEA-E811-99C7-001E675A6D10.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/84268E79-91EA-E811-84D6-001E67DDC0FB.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/90CFEBA1-79EA-E811-9CD5-485B3919F0DC.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/9CDA5728-6BEA-E811-BDE5-A4BF01027688.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/9EF93B22-85EA-E811-8157-001E67586629.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/A858B73F-92EA-E811-AF2F-001E67DDC254.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/B6C380BA-84EA-E811-8FED-001E67DFF609.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C29AD203-6BEA-E811-B999-001E67DDBFC5.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C4FDCFCC-5DEA-E811-BF9F-001E67DDD22B.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C85FC355-5DEA-E811-A095-001E67A3FB91.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C8E5EA4B-91EA-E811-8815-001E67DDC051.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/CA1C710E-5BEA-E811-9DB3-001E67A4061D.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/CED77EDB-93EA-E811-8A2D-001E67A3F3DF.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D0539975-89EA-E811-8404-001E67A3F8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D42BB2C5-85EA-E811-ABAD-001E67D195F0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/E4C135F5-81EA-E811-A7D6-001E67A4061D.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/EAA3C3D1-61EA-E811-BE07-001E675A68C4.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F09DF020-5EEA-E811-B472-A4BF0102A5F9.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F0FE466F-5DEA-E811-9849-001E675A6C2A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F22D228D-79EA-E811-B39A-001E67A3F70E.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F4F866AB-8AEA-E811-9366-A4BF01025C02.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F65D43D0-8BEA-E811-9E80-001E6758651B.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/FE7468C4-5DEA-E811-BCC3-001E67A3F8A8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/FEC7F7B1-88EA-E811-94C5-001517FB2458.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/009AA892-C8EA-E811-9BBB-001E675A6653.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/043F6BAC-DEEA-E811-A20E-001E67E5A38B.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/061364D4-9CEA-E811-A9C9-A4BF01013D80.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/0649D7CA-E8EA-E811-951B-001E67D8A423.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/0A737773-EFEA-E811-8CC9-EC0D9A04AE30.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/0C2159ED-BBEA-E811-AFFE-485B3919F0DC.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/0CAA3F1A-93EA-E811-8DF5-001E67A42175.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/0CB10097-A8EA-E811-BFB3-485B3919F0DC.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/0CE4E1E2-B1EA-E811-B99F-001E67DFF609.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/108A9DBE-F7EA-E811-AD88-001E67A3EA11.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/145BD714-E3EA-E811-9448-001E67D8A423.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/1A0C7D28-FAEA-E811-A0B1-001517FB141C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/1AE85D96-EDEA-E811-9FC7-001E67A4069F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/1E767AC2-CCEA-E811-85E9-A4BF01025766.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/247013E8-E5EA-E811-9375-001E67A3EC2D.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/260C8E9C-A0EA-E811-A2F1-001E67D8A423.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/262EF9DC-9BEA-E811-A229-001E675A6653.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2A26C3B0-C5EA-E811-86ED-A4BF01025766.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2A70CBF3-F8EA-E811-86A1-001E67A401B3.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2A71B9C0-9CEA-E811-88EA-A4BF01025C07.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2CAA1E90-AAEA-E811-87AE-001E67A3EA11.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/2CD83CB2-F0EA-E811-BBE4-001E67A40442.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/3040A0F0-E7EA-E811-B94D-A4BF01026229.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/32DF95C1-ADEA-E811-86A3-001E675A5244.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/38B2BB5D-A9EA-E811-9ACF-A4BF0126D535.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/3A8C63DB-E8EA-E811-BD73-001E67A4069F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/3AA53091-C0EA-E811-AFBB-485B3919F121.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/3AB8CBE7-E3EA-E811-BE28-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/40810615-A3EA-E811-9F69-A4BF01026229.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/44FE6565-9AEA-E811-ABC2-001E675A6928.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/46B2F9DA-94EA-E811-8E3D-001E67DDD348.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/4866D51A-7DEA-E811-BA3E-001E67E68BBD.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/50DF9F16-EAEA-E811-92FA-001E67DDD0AA.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/50E2BC24-ADEA-E811-B601-001E67DDCC81.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/5266AA7B-B0EA-E811-973A-001E67A401B3.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/5439F538-79EA-E811-9D6D-001E67E68BBD.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/543F0E77-D5EA-E811-ACB9-A4BF01025C07.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/58178CBD-A8EA-E811-AD91-001E67A4069F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/5A2901C3-F6EA-E811-AE5D-001E675A5244.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/5A603B7D-C1EA-E811-A684-A4BF01025C02.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/608E1C0B-A6EA-E811-A403-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/60B9A219-9BEA-E811-8802-001E67E69E32.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/62FF2FC4-98EA-E811-9761-A4BF01025766.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/66C4CDB0-C7EA-E811-BC81-001E67DDC051.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/68F13FA3-98EA-E811-96A0-A4BF01025766.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/6CA9BF2D-F0EA-E811-A62D-001517F807D4.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/70F19627-9CEA-E811-844F-001E67586629.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/76823CA0-B4EA-E811-907F-001E67E6965D.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/7AA8D3DE-E1EA-E811-90EF-001E67DDC6C8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/7C7F86BF-C5EA-E811-9305-001E67DDC6C8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/8046277E-D2EA-E811-893B-001E67A3EB1A.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/82017D2C-B7EA-E811-95C3-001E67DDD348.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/82F4EB04-E1EA-E811-9F77-001E67DFF4F6.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/840EECDD-A5EA-E811-A819-001E67A4069F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/866FC3CC-BDEA-E811-991D-001E67A404B0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/869DF4B9-ADEA-E811-A490-EC0D9A04AE30.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/86B429CA-DDEA-E811-805C-90B11C070100.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/86E6AFAD-A1EA-E811-94AF-001E67DFF4F6.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/888011C0-A0EA-E811-8AF7-001E67DFF609.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/8A401E3B-DEEA-E811-A53A-001E67D195F0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/8C40F2F1-9CEA-E811-8159-001E67E6920C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/8EB1D9C4-ECEA-E811-966D-A4BF0126D1BB.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/94611630-D5EA-E811-9269-001E67E6920C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/94947C3C-94EA-E811-84CC-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/94DEC44C-F6EA-E811-BCA4-001E67DDCC81.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/96355EA4-ACEA-E811-AA50-A4BF0126D1BB.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/9648E4B0-BBEA-E811-85EC-90B11C06954E.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/9A3C6B6C-6DEA-E811-B343-90B11C04FE38.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/9C3C73E0-BCEA-E811-84AC-90B11C06BDDA.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/9E12AEA4-D1EA-E811-A2A8-EC0D9A0B3320.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/9E508BEA-A7EA-E811-AB28-001E67DDD0AA.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/A2F112BF-E2EA-E811-9232-001E675A6AA9.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/A4C1416F-E1EA-E811-899C-001E67A3E8CC.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/A88E7C4E-B5EA-E811-8A85-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/B06D8407-C7EA-E811-80A3-EC0D9A0B3070.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/B26BBE18-9FEA-E811-BFC7-001E67A3EF48.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/B8F28FEA-EBEA-E811-82F1-A4BF0126D535.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/B8FDF71E-9FEA-E811-BE06-001E67DFF5D7.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/BA22D21B-BAEA-E811-97F8-001E67A40514.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/BCAD7E41-A6EA-E811-AFB4-EC0D9A0B3190.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C08DA26C-A0EA-E811-B826-001E67DDC6C8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C0B1328B-D2EA-E811-BF1C-A4BF01025C07.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C0CC7D5A-DEEA-E811-9081-001517F7F6A0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C2EC354F-8DEA-E811-AFB0-EC0D9A04AE30.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C4615CBE-D0EA-E811-BB24-001E67586629.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C4F33A99-94EA-E811-84CB-90B11C06BDDA.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C6CB1FF2-EFEA-E811-B12A-001E675A67BB.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/C6F1899F-B2EA-E811-A48C-001E675A6AB8.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/D4E88E41-ACEA-E811-9B85-001E67A40442.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/D6197AED-8CEA-E811-92C4-001E67A3E8F9.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/D69A559F-9CEA-E811-8ED2-001E67E5A38B.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/D8F2678D-E7EA-E811-B63E-EC0D9A0B3190.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/DC7A289E-9EEA-E811-9DA3-001E67D195F0.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/DE9A2763-8BEA-E811-865D-A4BF0101202F.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/E0F8D024-D9EA-E811-B367-A4BF01013D80.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/E2255756-A7EA-E811-B960-001E67A42026.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/E68CDE54-84EA-E811-AA4F-001E675A6725.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/E6A93E2A-A0EA-E811-9E44-001E67D8A423.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/E6B97078-9CEA-E811-A668-EC0D9A0B3320.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/EA885AAC-B0EA-E811-AD67-001E675A6A63.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/ECB5A53A-F3EA-E811-BF2A-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/F0DCDF14-D7EA-E811-93B7-A4BF0101F533.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/F4C11BA7-B1EA-E811-B896-001517FB141C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/270000/F4DE74E7-A0EA-E811-8E12-001E675A6AA9.root',
] )
